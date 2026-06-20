@echo off
echo ========================================
echo Starting CarbonTracker AI Backend
echo ========================================
echo.

cd backend
call venv\Scripts\activate.bat
echo Backend server starting on http://localhost:8000
echo API docs available at http://localhost:8000/docs
echo.
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

@REM Made with Bob
