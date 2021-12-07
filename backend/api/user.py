from typing import List
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from backend.schemas import UserSchema, UserRegisterCode
from backend.models import get_db, Users
user_router = APIRouter(prefix='/user')


def generate_code():
    pass


def exists_user(db: Session, email: str):
    return db.query(Users).filter(Users.mail == email).first()


def get_db_user(db: Session, uuid: str):
    return db.query(Users).filter(Users.uuid == uuid).first()


def exists_user_and_verified(db: Session, email: str):
    user = db.query(Users).filter(Users.mail == email).first()
    if user.code:
        if user.code.is_verified:
            return True
    return False


@user_router.post('/code')
def new_code(user: UserRegisterCode, db: Session = Depends(get_db)):
    if exists_user_and_verified(db, user.mail):
        raise HTTPException(status_code=400, detail='Email Already Registered and Verified')
    generate_code()
    return JSONResponse(status_code=200, content='Code Sent to the registered Email')


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
    user = get_db_user(db, uuid)
    if not user:
        raise HTTPException(status_code=404, detail='User not found!')
    return user


@user_router.delete('/{uuid}')
def delete_user(uuid: str, db: Session = Depends(get_db)):
    user = get_db_user(db, uuid)
    if not user:
        raise HTTPException(status_code=404, detail='User not found!')
    db.delete(user)
    db.commit()
    return JSONResponse(status_code=200, content='User Deleted')
