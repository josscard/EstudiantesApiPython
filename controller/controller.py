from fastapi import FastAPI, HTTPException, APIRouter
from typing import List

from model.models import AdvisorySession, Student
from service.service import AdvisorySessionService

# Crear la instancia de FastAPI y el servicio

router = APIRouter()
session_service = AdvisorySessionService()


# Ruta GET: Listar todas las sesiones
@router.get("/sessions", response_model=List[AdvisorySession])
def get_all_sessions():
    return session_service.get_all_sessions()

# Ruta POST: Crear una nueva sesión
@router.post("/sessions", status_code=201)
def create_session(session: AdvisorySession):
    session_service.add_session(session)
    return {"message": "Session created successfully"}

#Listar Estudiantes

@router.get("/students", response_model=List[Student])
def get_all_students():
    return session_service.get_all_students()

#Crear estudiante
@router.post("/students", status_code=201)
def create_student(student: Student):
    session_service.add_student(student)
    return {"message": "Student created successfully"}