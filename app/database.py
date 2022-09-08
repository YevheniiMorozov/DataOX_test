from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# if use script
# from decouple import config
#
#
# DB_USER = config("DB_USER")
# DB_PASS = config("DB_PASS")
# IP = config("IP")
# DB_NAME = config("DB_NAME")

DB_USER = "docker"
DB_PASS = 'docker'
IP = "0.0.0.0"
DB_NAME = "apartments"

POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASS}@{IP}/{DB_NAME}"


engine = create_engine(POSTGRES_URI)
Session = sessionmaker()
