@echo off
:: Obtiene la fecha en formato YYYYMMDD
for /f "tokens=2-4 delims=/ " %%a in ('echo %date%') do set fecha=%%c%%b%%a

:: Cambia al directorio donde está instalado MySQL
cd C:\Program Files\MySQL\MySQL Server 9.0\bin

:: Elimina copias de seguridad antiguas
del /Q C:\Backup\*.sql

:: Crea la nueva copia de seguridad
mysqldump -u root --password=170311 library > C:\Backup1\library_%fecha%.sql
