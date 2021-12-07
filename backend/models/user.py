from backend.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
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


class Code(Base):
    """ Code model."""
    __table_name__ = 'code'

    id = Column(Integer, primary_key=True)
    unique_code = Column(String, nullable=False, unique=True)
    is_expired = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    user = relationship('Users', backref='code', uselist=False)

    def __repr__(self) -> str:

        return f"<Code {self.unique_code}>"