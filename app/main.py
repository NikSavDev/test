from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, database
from .database import SessionLocal
#from fastapi.responses import JSONResponse

@asynccontextmanager
async def lifespan():
    # Startup event
    database.init_db()
    yield
    # Shutdown event
    #pass

app = FastAPI(lifespan=lifespan)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/posts", response_model=list[schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@app.get("/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/posts", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)

@app.put("/posts/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    updated_post = crud.update_post(db=db, post_id=post_id, post=post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@app.delete("/posts/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    deleted_post = crud.delete_post(db=db, post_id=post_id)
    if deleted_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return deleted_post
