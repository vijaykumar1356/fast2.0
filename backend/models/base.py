from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from typing import Any

# engine = create_engine('sqlite:///./sqlite.db', echo=True)
engine = create_engine('postgresql://pitch_dev:nytro123@localhost:5432/poc')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Base.metadata.tables
# Base.metadata.create_all(bine=engine)


# from sqlalchemy.ext.declarative import as_declarative, declared_attr
# from typing import Any


# @as_declarative()
# class Base:
#     id: Any
#     __name__: str
#     # Generate __tablename__ automatically
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()
