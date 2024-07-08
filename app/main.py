from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from contextlib import asynccontextmanager
from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/posts/", response_model=List[schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@app.get("/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)

@app.put("/posts/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.update_post(db=db, post_id=post_id, post=post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.delete("/posts/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.delete_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.get("/posts/search", response_model=List[schemas.Post])
def search_posts(query: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = crud.search_posts(db, query=query, skip=skip, limit=limit)
    return posts
