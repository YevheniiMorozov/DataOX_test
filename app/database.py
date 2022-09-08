from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from decouple import config


DB_USER = config("DB_USER")
DB_PASS = config("DB_PASS")
IP = config("IP")
DB_NAME = config("DB_NAME")

POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASS}@{IP}/{DB_NAME}"


engine = create_engine(POSTGRES_URI)
Session = sessionmaker()
