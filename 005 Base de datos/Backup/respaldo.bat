@echo off
:: Obtiene la fecha en formato YYYYMMDD
for /f "tokens=2-4 delims=/ " %%a in ('echo %date%') do set fecha=%%c%%b%%a

cd C:\Program Files\MySQL\MySQL Server 9.0\bin
mysqldump -u root --password=170311 library > C:\Backup\library_%fecha%.sql
