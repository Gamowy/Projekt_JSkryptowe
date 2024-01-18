@echo off
setlocal EnableDelayedExpansion
@chcp 1250
:menu
cls
echo ^|====================================^|
echo ^| Zadanie 2 2014 - Kó³ko i Krzy¿yk   ^|
echo ^|====================================^|
echo ^|1.Wykonaj obliczenia                ^|
echo ^|2.Za³aduj dane wejœciowe            ^|
echo ^|3.Wygeneruj raport                  ^|
echo ^|4.Otwórz raport                     ^|
echo ^|5.Koniec                            ^|
echo ^|====================================^|
set /p choice=^|Wybór:
if "%choice%"=="1" ( goto :opcja1 )
if "%choice%"=="2" ( goto :opcja2 )
if "%choice%"=="3" ( goto :opcja3 )
if "%choice%"=="4" ( goto :opcja4 )
if "%choice%"=="5" ( goto :eof) else ( goto :menu )

:opcja1
    if defined input (
        set /a i=0
        cd /d "%input%"
        for /r %%x in (*.txt) do (
            py "%~dp0\src\SolveBoard.py" "%%x" "%~dp0out\out!i!.txt"
            if exist "%~dp0out\out!i!.txt" set /a i=!i!+1
        )
        cd /d "%~dp0"
        echo Wykonano obliczenia na plikach z katalogu %input%
    ) else (
        echo Nie za³adowano katalogu z danymi wejœciowymi
    )
    pause
    goto :menu
:opcja2
    set /p input=Podaj scie¿kê katalogu z danymi wejœciowymi:
    if exist %input% (
        echo Pomyœlnie za³adowano katalog %input%
    ) else (
        echo Nie uda³o siê za³adowaæ katalogu %input%
    )
    pause
    goto :menu
:opcja3
    py "%~dp0\src\RaportGen.py" "%~dp0out" "raport.html"
    pause
    goto :menu
:opcja4
    if exist raport.html (
        echo Otwieram plik raport.html
        start raport.html
    ) else (
        echo Nie znaleziono raportu
    )
    pause
    goto :menu