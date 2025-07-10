# In file: main.py

from fastapi import FastAPI
from api.routes import students

app = FastAPI(
    title="Student Management API",
    description="A refactored API to manage students with Ollama integration.",
    version="2.0.0"
)

app.include_router(students.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Student Management API!"}