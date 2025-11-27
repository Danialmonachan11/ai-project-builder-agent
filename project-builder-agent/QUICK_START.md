# Project Builder Agent - Quick Start Guide

## 🚀 Three Ways to Run

### Option 1: Single Command (Easiest!) ⭐
**Just double-click `START_ALL.bat`**

This will:
- Open 2 separate terminal windows (one for backend, one for frontend)
- Install all dependencies automatically
- Start both servers
- Show you the URLs to access

Then open your browser to: **http://localhost:5173**

---

### Option 2: Docker Compose (Recommended for Production)
If you have Docker installed:

```bash
docker-compose up
```

That's it! Both services will start in containers.
Open: **http://localhost:5173**

To stop:
```bash
docker-compose down
```

---

### Option 3: Manual (For Debugging)
If you need to debug or prefer manual control:

**Terminal 1 - Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## 🎯 What You'll See

1. **Backend** starts on `http://localhost:8000`
   - API documentation: `http://localhost:8000/docs`

2. **Frontend** starts on `http://localhost:5173`
   - This is the main UI you'll use

## 💡 Tips

- **First time setup**: The first run takes longer (installing dependencies)
- **Keep windows open**: Don't close the terminal windows while using the app
- **Restart**: If something breaks, just close everything and run `START_ALL.bat` again

## 🐛 Troubleshooting

**Backend won't start:**
- Check if Python is installed: `python --version`
- Check if port 8000 is available

**Frontend won't start:**
- Check if Node.js is installed: `node --version`
- Try: `cd frontend && npm install --legacy-peer-deps`

**Still not working?**
- Delete `frontend/node_modules` folder and try again
- Make sure no other apps are using ports 8000 or 5173
