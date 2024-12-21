@echo off

:: Inicia el frontend en segundo plano
start javaw -jar "C:\Ejecutables\Biblioteca-1.0-SNAPSHOT-jar-with-dependencies.jar"

:: Espera un momento para asegurar que el frontend esté ejecutándose
timeout /t 2

:: Inicia el backend en segundo plano (sin consola)
start javaw -jar "C:\Ejecutables\library-0.0.1-SNAPSHOT.jar"

:: Obtiene el PID del frontend (javaw.exe para Biblioteca)
for /f "tokens=2" %%i in ('tasklist /FI "IMAGENAME eq javaw.exe" /FI "WINDOWTITLE eq Biblioteca" /NH') do set FRONTEND_PID=%%i

:: Obtiene el PID del backend (javaw.exe para library)
for /f "tokens=2" %%i in ('tasklist /FI "IMAGENAME eq javaw.exe" /FI "WINDOWTITLE eq library" /NH') do set BACKEND_PID=%%i

:: Monitorea si el proceso del frontend sigue ejecutándose
:monitor
tasklist /FI "PID eq %FRONTEND_PID%" | findstr /i "javaw.exe" > nul
if %ERRORLEVEL% equ 0 (
    :: Si el frontend está ejecutándose, espera 5 segundos y vuelve a comprobar
    timeout /t 5
    goto monitor
) else (
    :: Si el frontend se cerró, termina solo el backend
    taskkill /F /PID %BACKEND_PID% /T
    echo El frontend se cerró. El backend también se detuvo.
)

exit


