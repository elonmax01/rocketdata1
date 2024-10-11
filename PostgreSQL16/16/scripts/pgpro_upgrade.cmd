@echo off
if "%PGDATA%"=="" set PGDATA=%~1
if "%PGDATA%"=="" set PGDATA=C:\projects\testrocketdata\PostgreSQL16\data
PATH C:\projects\testrocketdata\PostgreSQL16\16\bin;%PATH%
rem if exist "C:\projects\testrocketdata\PostgreSQL16\16\bin\pgpro_upgrade" sh.exe "C:\projects\testrocketdata\PostgreSQL16\16\bin\pgpro_upgrade"
