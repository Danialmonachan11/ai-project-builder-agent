# Quick Start Guide

## Prerequisites
Make sure you have installed:
- **Python 3.9+** (Download from https://www.python.org/)
- **Node.js & npm** (Download from https://nodejs.org/)

## Easy Startup (Using Batch Files)

1. **Double-click `START_BACKEND.bat`**
   - This will install Python dependencies and start the backend server
   - Wait until you see "Uvicorn running on http://0.0.0.0:8000"
   - Keep this window open!

2. **Double-click `START_FRONTEND.bat`** (in a new window)
   - This will install npm packages and start the frontend
   - Wait until you see "Local: http://localhost:5173/"
   - Keep this window open!

3. **Open your browser** and go to `http://localhost:5173`

## Manual Startup (If batch files don't work)

### Terminal 1 - Backend:
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Terminal 2 - Frontend:
```bash
cd frontend
npm install
npm run dev
```

## Troubleshooting

### Backend Issues:
- **"uvicorn: command not found"**: Run `pip install uvicorn`
- **Port 8000 already in use**: Change port in `START_BACKEND.bat` to `--port 8001`

### Frontend Issues:
- **"npm: command not found"**: Make sure Node.js is installed
- **npm install hangs**: Try `npm install --legacy-peer-deps`
- **Port 5173 already in use**: The app will automatically use the next available port

### Still not working?
Please send me a screenshot of the error message you're seeing!
