@echo off
echo ========================================
echo CarbonTracker AI - Setup Script
echo ========================================
echo.

echo [1/4] Setting up Backend...
cd backend
echo Creating Python virtual environment...
python -m venv venv
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.
echo Installing Python dependencies...
pip install --upgrade pip
pip install -r requirements.txt
echo Backend setup complete!
echo.
cd ..

echo [2/4] Setting up Frontend...
cd frontend
echo Installing Node.js dependencies...
call npm install
echo Frontend setup complete!
echo.
cd ..

echo [3/4] Creating environment files...
if not exist "frontend\.env.local" (
    copy "frontend\.env.local.example" "frontend\.env.local"
    echo Created frontend/.env.local
)
echo.

echo [4/4] Creating necessary directories...
if not exist "backend\uploads" mkdir "backend\uploads"
if not exist "backend\app\ml\models" mkdir "backend\app\ml\models"
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the application:
echo   1. Run: start-backend.bat
echo   2. Run: start-frontend.bat
echo.
echo Or use: start-all.bat to start both
echo.
pause

@REM Made with Bob
