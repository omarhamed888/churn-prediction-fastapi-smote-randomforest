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

---

## Model Input Format

### API Input (CustomerData)
When using the `/predict` endpoint, send a JSON body with the following fields:
```json
{
  "CreditScore": 650,
  "Geography": "France",
  "Gender": "Female",
  "Age": 35,
  "Tenure": 5,
  "Balance": 75000.0,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 50000.0
}
```
The backend will preprocess this data (including one-hot encoding and log transforms) before prediction.

### Processed Feature Format
After preprocessing, the model expects features like:
- Age
- EstimatedSalary
- Balance
- CreditScore
- Age_log
- NumOfProducts
- Tenure
- IsActiveMember
- Geography_Germany
- Gender_Male
- HasCrCard
- Geography_Spain

You do **not** need to provide these directly when using the API, but you may use this format for direct testing in the notebook.

---

## Testing the Model in the Notebook

1. Open `notebook/fnotebook.ipynb`.
2. Use the provided cells to load the preprocessor and model, create a sample input, and make a prediction.
3. You can test both the original and processed formats as shown in the notebook.
