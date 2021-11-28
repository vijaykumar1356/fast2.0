from backend.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean


class Users(Base):
    """ User model."""

    id = Column(Integer, primary_key=True)
    mail = Column(String, nullable=False)
    full_name = Column(String)
    unique_id = Column(String, nullable=False, unique=True)
    profile_pic = Column(String)
    password = Column(String)
    oauth_verfied = Column(Boolean, default=False)

    def __repr__(self) -> str:

        return f"<User {self.full_name}>"
