@echo off
@REM cd /d "%~dp0ITMO\OPD"
start powershell.exe -NoExit -Command "cd .. ; java -Dmode=dual -jar .\bcomp-ng.jar"