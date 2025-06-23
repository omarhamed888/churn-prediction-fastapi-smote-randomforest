# Churn Prediction API

This project is a Python-based machine learning API using FastAPI. It includes dependencies for data science, model training, and serving predictions.

## Setup
1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Running the API
To run the FastAPI server:
```powershell
uvicorn main:app --reload
```

Replace `main:app` with your actual entrypoint if different.
