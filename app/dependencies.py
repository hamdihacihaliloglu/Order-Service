import json
import os
import random
import secrets
import string
import uuid
from time import time

import requests
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.config.database import SessionLocal
from app.config.settings import settings

def get_db():
    global db
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
