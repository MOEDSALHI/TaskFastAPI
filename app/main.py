from fastapi import FastAPI

from app.database import Base, engine
from app.routers import project, task, user

app = FastAPI()

# Inclusion des routeurs
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(project.router, prefix="/projects", tags=["Projects"])
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])
