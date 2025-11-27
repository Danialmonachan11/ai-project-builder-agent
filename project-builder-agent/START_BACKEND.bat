@echo off
echo ========================================
echo Installing Backend Dependencies...
echo ========================================
cd backend
pip install -r requirements.txt
echo.
echo ========================================
echo Starting Backend Server...
echo ========================================
echo Backend will run on http://localhost:8000
echo.
uvicorn main:app --reload --port 8000
pause
