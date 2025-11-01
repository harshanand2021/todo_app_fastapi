from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status, Path
import models
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

class TodoBase(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool
    
class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    
    class Config:
        from_attributes = True


@app.get("/", response_model=list[Todo])
async def read_all(db: db_dependency):
    return db.query(models.Todos).all()

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK, response_model=Todo)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")

@app.post("/todo", status_code=status.HTTP_201_CREATED, response_model=Todo)
async def create_todo(db: db_dependency, todo_request: TodoCreate):
    todo_model = models.Todos(**todo_request.model_dump())
    
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model
    
@app.put("/todo/{todo_id}", status_code=status.HTTP_200_OK, response_model=Todo)
async def update_todo(db: db_dependency, todo_request: TodoCreate, todo_id: int = Path(gt=0)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    
    if todo_model is None:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    
    db.add(todo_model)
    db.commit()
    
@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    
    if todo_model is None:
        raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")
    
    db.delete(todo_model)
    db.commit()
    
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)