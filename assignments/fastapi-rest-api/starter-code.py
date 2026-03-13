# Starter code for FastAPI REST API assignment

# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Add your endpoints and logic below
