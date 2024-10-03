import sqlalchemy
from sqlalchemy import event
from sqlalchemy.orm import registry, Session


mapper_registry = registry()
Base = mapper_registry.generate_base()