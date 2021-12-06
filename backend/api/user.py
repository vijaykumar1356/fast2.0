from typing import List
from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from backend.schemas import UserSchema
from backend.models import get_db, Users
user_router = APIRouter(prefix='/user')


def exists_user(db: Session, email: str):
    return db.query(Users).filter(Users.mail == email).first()


def get_db_user(db: Session, uuid: str):
    return db.query(Users).filter(Users.uuid == uuid).first()


@user_router.post('/register', response_model=UserSchema)
def register(user: UserSchema, db: Session = Depends(get_db)):
    if exists_user(db, user.mail):
        raise HTTPException(status_code=400, detail='Email already registered!')
    db_user = Users(
        mail=user.mail, password=user.password, full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@user_router.get('/', response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(Users).all()


@user_router.get('/{uuid}', response_model=UserSchema)
def get_user(uuid: str, db: Session = Depends(get_db)):
    return get_db_user(db, uuid)
