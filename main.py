from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from src.utils.db import Base, engine
from src.utils.settings import settings
from src.tasks.router import task_routes

from src.users.router import user_routes
Base.metadata.create_all(engine)
app = FastAPI(title="This is my task management Application")

origins = [o.strip() for o in settings.ALLOWED_ORIGINS.split(",")]
app.add_middleware(                                 
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_routes)
app.include_router(user_routes)


