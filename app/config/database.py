from os import environ

from sqlalchemy import create_engine, NullPool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from app.config.settings import settings

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://" + environ.get('DB_USER') + ":" + environ.get('DB_PASS') + \
                          "@" + environ.get('DB_HOST') + ":" + environ.get('DB_PORT') + "/" + environ.get('DB_NAME')

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=30, max_overflow=60, pool_recycle=200, pool_pre_ping=True)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = scoped_session(session_factory)

Base = declarative_base()