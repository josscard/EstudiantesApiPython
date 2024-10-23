
from fastapi import FastAPI
from controller.controller import router as session_router

app = FastAPI()

app.include_router(session_router, prefix="/api/university/advisors")







