# In file: api/routes/students.py

from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from schemas.student import Student, StudentCreate, StudentUpdate
from core import db
from services import ollama

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

def find_student_or_404(student_id: int) -> Student:
    student = db.get_student_by_id_from_db(student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

@router.post("", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student_in: StudentCreate):
    return db.create_student_in_db(student_in)

@router.get("", response_model=List[Student])
def get_all_students():
    return db.get_all_students_from_db()

@router.get("/{student_id}", response_model=Student)
def get_student_by_id(student: Student = Depends(find_student_or_404)):
    return student

@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student_in: StudentUpdate):
    updated_student = db.update_student_in_db(student_id, student_in)
    if not updated_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return updated_student

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    if not db.delete_student_from_db(student_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return

@router.get("/{student_id}/summary", response_model=dict)
async def generate_summary(student: Student = Depends(find_student_or_404)):
    summary = await ollama.generate_summary_from_ollama(student)
    return {"student_id": student.id, "summary": summary}