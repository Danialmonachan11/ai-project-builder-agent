# 🐛 Debugging Guide for 500 Errors

## What I Just Fixed:

✅ **Missing `.github/workflows/` directory** - The code tried to write a GitHub Actions file without creating the directory first.

## How to See the Actual Error:

1. **Look at your backend terminal window** - it should show the full error message with traceback
2. The error will tell you exactly what went wrong

## Common 500 Error Causes:

### 1. Missing Directory
**Error**: `FileNotFoundError: [Errno 2] No such file or directory`
**Fix**: Code now creates all directories before writing files

### 2. Import Error  
**Error**: `ModuleNotFoundError: No module named 'xyz'`
**Fix**: Run `pip install -r requirements.txt` in the backend folder

### 3. Syntax Error in Generated Code
**Error**: `SyntaxError: invalid syntax`
**Fix**: Check the backend terminal for the line number

## Quick Restart:

1. **Close all terminal windows**
2. **Double-click `START_ALL.bat` again**
3. **Try generating a project**
4. **If error persists, check the backend terminal for the error message**

---

**The directory creation bug is now fixed!** Restart your backend and try again.
