import os
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routers import KPI_router
from app.settings.database import init_db

app = FastAPI()
init_db()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = os.getenv("ALLOWED_ORIGINS"),
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(KPI_router.router)

