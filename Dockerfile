# 1. Base image
FROM python:3.10-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency list
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code and model
COPY deployment.py .
COPY titanic_xgb_v1.pkl .

# 6. Expose port FastAPI will run on
EXPOSE 80

# 7. Start FastAPI using uvicorn
CMD ["uvicorn", "deployment:app", "--host", "0.0.0.0", "--port", "80"]
