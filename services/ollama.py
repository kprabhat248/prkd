# In file: services/ollama.py

import httpx
from fastapi import HTTPException, status
from schemas.student import Student

OLLAMA_API_URL = "http://host.docker.internal:11434/api/generate"

async def generate_summary_from_ollama(student: Student) -> str:
    prompt = f"""
    Based on the following student details, please generate a short, professional,
    and engaging summary (one paragraph) for a student profile.
    Do not just list the details, but create a narrative.

    Student Details:
    - Name: {student.name}
    - Age: {student.age}

    Now, generate a new summary for this student:
    """

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False,
    }
    
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(OLLAMA_API_URL, json=payload)
            response.raise_for_status()
            return response.json().get("response", "No summary could be generated.")
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Could not connect to Ollama service: {e}"
        )