from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Blog import models, schemas
from Blog.routers import blog  # Correct import
from Blog.routers import user
from .. import database

router = APIRouter(
    prefix="/user",
    tags = ['users'])

get_db = database.get_db
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)  # Correct function call
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)