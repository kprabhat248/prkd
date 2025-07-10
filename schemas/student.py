

from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    age: int
    email: EmailStr

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    email: EmailStr | None = None

class Student(StudentCreate):
    id: int