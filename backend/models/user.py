from backend.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean
from uuid import uuid4


class Users(Base):
    """ User model."""

    id = Column(Integer, primary_key=True)
    mail = Column(String, nullable=False)
    full_name = Column(String)
    uuid = Column(String, nullable=False, default=uuid4().hex)
    profile_pic = Column(String)
    password = Column(String)
    oauth_verfied = Column(Boolean, default=False)

    def __repr__(self) -> str:

        return f"<User {self.full_name}>"
