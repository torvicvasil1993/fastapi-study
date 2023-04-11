"""
postgresql:
https://dev.to/andre347/how-to-easily-create-a-postgres-database-in-docker-4moj

docker run --name postgres-db -e POSTGRES_PASSWORD=docker -p 5432:5432 -d postgres

Host: localhost
Port: 5432
User: postgres
Password: docker




"""

from fastapi import FastAPI, Depends
import models
from database import engine, SessionLocal
from routers import auth, todos, users
from company import companyapis, dependencies

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(
    companyapis.router,
    prefix="/companyapis",
    tags=["companyapis"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={418: {"description": "Internal Use Only"}}
)
app.include_router(users.router)


