from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: Optional[int]
    uuid: Optional[str]
    mail: str
    full_name: str
    password: str

    class Config:
        orm_mode = True
