@echo off
echo ========================================
echo    Project Builder Agent - Launcher
echo ========================================
echo.
echo Starting Backend and Frontend...
echo.

REM Start backend in a new window
start "Backend Server" cmd /k "cd backend && pip install -r requirements.txt && uvicorn main:app --reload --port 8000"

REM Wait 3 seconds for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend in a new window
start "Frontend Server" cmd /k "cd frontend && call npm install && call npm run dev"

echo.
echo ========================================
echo   Both servers are starting!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173
echo.
echo Keep both windows open while using the app.
echo Close this window when done.
echo ========================================
pause
