@echo off
chcp 1251
PATH C:\projects\testrocketdata\PostgreSQL16\16\bin;%PATH%
if not exist "%APPDATA%\postgresql" md "%APPDATA%\postgresql"
psql.exe -h localhost -U "postgres" -d postgres -p 5432 
pause