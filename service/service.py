from model.models import AdvisorySession, Student, ProjectAdvisory, AcademicAdvisory, Advisor
from typing import List, Optional
from datetime import datetime

class AdvisorySessionService:
    def __init__(self):
        self.sessions: List[AdvisorySession] = []
        self.students: List[Student] = []
        self.load_default_sessions()



    def load_default_sessions(self):
        # Estudiantes y asesores de ejemplo
        alice = Student(id="S1", name="Alice")
        bob = Student(id="S2", name="Bob")
        self.students.extend([alice, bob])

        dr_smith = Advisor(id="A1", name="Dr. Smith")
        prof_johnson = Advisor(id="A2", name="Prof. Johnson")

        
        # Agregar sesiones de ejemplo
        self.sessions.append(AcademicAdvisory(
            id="AS1", student=alice, advisor=dr_smith,
            date_time=datetime(2024, 10, 25, 10, 0)
        ))

        self.sessions.append(ProjectAdvisory(
            id="AS2", student=bob, advisor=prof_johnson,
            date_time=datetime(2024, 10, 27, 14, 0),
            project_title="Intelligent Campus System"
        ))



    def get_all_sessions(self) -> List[AdvisorySession]:
        return self.sessions





    def add_student(self, student: Student):
        self.students.append(student)

    def add_session(self, session: AdvisorySession):
        # Verificar si el estudiante ya existe, si no, crearlo
        student = self.find_or_create_student(session.student)
        session.student = student  # Asignar el estudiante actualizado
        self.sessions.append(session)

    def find_or_create_student(self, student: Student) -> Student:
        # Buscar si el estudiante ya existe
        existing_student = self.get_student_by_id(student.id)
        if existing_student:
            return existing_student
        # Si no existe, añadir el estudiante a la lista
        self.students.append(student)
        return student

    def get_student_by_id(self, student_id: str) -> Optional[Student]:
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def get_all_students(self) -> List[Student]:
        return self.students


