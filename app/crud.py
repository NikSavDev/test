from sqlalchemy.orm import Session
from . import models, schemas

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).offset(skip).limit(limit).all()

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post_id: int, post: schemas.PostCreate):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        return None
    for key, value in post.dict().items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        return None
    db.delete(db_post)
    db.commit()
    return db_post

def search_posts(db: Session, query: str, skip: int = 0, limit: int = 10):
    return db.query(models.Post).filter(
        models.Post.title.contains(query) | models.Post.content.contains(query)
    ).offset(skip).limit(limit).all()
