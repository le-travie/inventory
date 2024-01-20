from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

host = config("HOST")
user = config("USER")
pwd = config("PWD")
port = config("PORT")
db = config("DB")

db_url = f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}"
db_engine = create_engine(db_url, echo=True)

MasterSession = sessionmaker(bind=db_engine, autocommit=False)


class Base(DeclarativeBase):
    pass
