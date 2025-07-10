

import threading
from typing import List, Dict, Optional
from schemas.student import Student, StudentCreate, StudentUpdate

_db: Dict[int, Student] = {}
_next_id = 1
_lock = threading.Lock()

def create_student_in_db(student_in: StudentCreate) -> Student:
    global _next_id
    with _lock:
        new_id = _next_id
        student = Student(id=new_id, **student_in.dict())
        _db[new_id] = student
        _next_id += 1
        return student

def get_all_students_from_db() -> List[Student]:
    with _lock:
        return list(_db.values())

def get_student_by_id_from_db(student_id: int) -> Optional[Student]:
    with _lock:
        return _db.get(student_id)

def update_student_in_db(student_id: int, student_in: StudentUpdate) -> Optional[Student]:
    with _lock:
        if student_id not in _db:
            return None
        existing_student = _db[student_id]
        update_data = student_in.dict(exclude_unset=True)
        updated_student = existing_student.copy(update=update_data)
        _db[student_id] = updated_student
        return updated_student

def delete_student_from_db(student_id: int) -> bool:
    with _lock:
        if student_id in _db:
            del _db[student_id]
            return True
        return False