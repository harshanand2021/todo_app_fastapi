from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from models import Todos
from database import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
db_dependency = Annotated[Session, Depends(get_db)]
        
        
@router.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@router.get("/todo/{todo_id}")
async def read_todo(db: db_dependency, todo_id: int):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")