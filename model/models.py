from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Student(BaseModel):
    id: str
    name: str

class Advisor(BaseModel):
    id: str
    name: str

class  AdvisorySession(BaseModel):
    id: str
    student: Student
    advisor: Advisor
    date_time: datetime


# Especialización para sesiones académicas
class AcademicAdvisory(AdvisorySession):
    pass


 # Título del proyecto, solo para esta especialización
class ProjectAdvisory(AdvisorySession):
    project_title: Optional[str] = None