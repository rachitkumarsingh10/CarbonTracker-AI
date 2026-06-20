@echo off
echo ========================================
echo Starting CarbonTracker AI
echo ========================================
echo.
echo Starting Backend and Frontend servers...
echo.

start "CarbonTracker Backend" cmd /k start-backend.bat
timeout /t 3 /nobreak >nul
start "CarbonTracker Frontend" cmd /k start-frontend.bat

echo.
echo Both servers are starting in separate windows.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Press any key to exit this window...
pause >nul

@REM Made with Bob
