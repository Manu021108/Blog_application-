from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from Blog import models, schemas
from Blog.database import engine, get_db
from passlib.context import CryptContext
from Blog.routers import blog, user, authentication  # Correct import

app = FastAPI(
    tags=['Authentication']
)


models.Base.metadata.create_all(bind=engine)


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)

