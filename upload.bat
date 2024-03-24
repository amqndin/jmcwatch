
@echo off

rd /S /Q "./build" >nul
rd /S /Q "./dist" >nul
rd /S /Q "./jmcwatch.egg-info" >nul

echo Press Enter to insert the saved PyPI token.
echo Press any other key to insert it manually.
set /p input=

if not defined input (
    for /f "tokens=1 delims=" %%a in (../pypi_token.txt) do set pypi_token=%%a
) else (
    set /p pypi_token=Enter PyPI token manually:
)

python setup.py sdist
twine upload dist/* -u __token__ -p %pypi_token%
