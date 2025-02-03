import os

from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine


from sqlalchemy.orm import declarative_base, sessionmaker

# Charger le bon fichier .env en fonction de l'environnement
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
dotenv_path = f".env.{ENVIRONMENT}"
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL est manquant dans le fichier .env")


engine = create_engine(DATABASE_URL)
metadata = MetaData()
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
