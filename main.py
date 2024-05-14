from fastapi import FastAPI
from app.routers import KPI_router
from app.settings.database import exec_sql_file

app = FastAPI()
exec_sql_file("app/scripts/init.sql")

app.include_router(KPI_router.router) 