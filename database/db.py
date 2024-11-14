import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

db_name = "my_db.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()
engine = create_engine(url=f"sqlite:///{db_name}", echo=True)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass

def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
