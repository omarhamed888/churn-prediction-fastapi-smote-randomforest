# Churn Prediction API

This project is a Python-based machine learning API using FastAPI. It includes dependencies for data science, model training, and serving predictions.

## Setup
1. Create and activate a virtual environment (recommended name: `.venv`):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate
   # Or, in PowerShell:
   .\.venv\Scripts\Activate
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
   If you add new packages, update requirements.txt with:
   ```powershell
   pip freeze > requirements.txt
   ```

## Running the API
To run the FastAPI server:
```powershell
python -m uvicorn main:app --reload
```
If you get a 'uvicorn not recognized' error, make sure your virtual environment is activated and dependencies are installed.

- The API docs are available at: http://127.0.0.1:8000/docs

Replace `main:app` with your actual entrypoint if different.
