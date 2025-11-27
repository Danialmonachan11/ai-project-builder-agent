@echo off
echo ========================================
echo Installing Frontend Dependencies...
echo ========================================
cd frontend
call npm install
echo.
echo ========================================
echo Starting Frontend Server...
echo ========================================
echo Frontend will run on http://localhost:5173
echo.
call npm run dev
pause
