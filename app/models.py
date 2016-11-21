import re
import datetime
from database import db
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Entry(Base):
    __tablename__ = 'Entry'
    title = Column('Title', String(), nullable=False)
    slug = Column('Slug', String(), primary_key=True, nullable=False)
    timestamp = Column('Timestamp', DateTime, default=datetime.datetime.now, index=True, nullable=False)

    def __init__(self, title, slug, content, published, timestamp):
        self.title = title
        self.slug = slug
        self.content = content
        self.published = published
        self.timestamp = timestamp

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)