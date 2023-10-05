@echo off
color 0a

cd dependencies

echo installing python...
call install_python.bat

echo.
echo Installing Python packages from requirements.txt...
pip install -r requirements.txt

if %errorlevel% equ 0 (
  echo Installation completed successfully.
) else (
  echo An error occurred during installation.
)

pause