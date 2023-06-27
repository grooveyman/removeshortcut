@echo off
set /p input = Enter drive name
for %%a in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do vol %%a: 2>nul | find "%input%" >nul && set myDrive=%%a:
if "%myDrive%"=="" (echo Cannot find volume
) else (
echo Drive letter is %myDrive%)
)

attrib -h -r -s /s /d  %myDrive%\*.*
del %myDrive%"\*.lnk" 2>logfile.txt
del %myDrive%"\$RECYCLER.BIN" 2>logfile.txt
pause
