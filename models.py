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
    title = Column('Title', String())
    slug = Column('Slug', String(), primary_key=True)
    content = Column('Content', String())
    published = Column('Published', Boolean())
    timestamp = Column('Timestamp', DateTime, default=datetime.datetime.now, index=True)

    def __init__(self, title, slug, content, published, timestamp):
        self.title = title
        self.slug = slug
        self.content = content
        self.published = published
        self.timestamp = timestamp

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = re.sub('[^\w]+', '-', self.title.lower())
    #     ret = super(Entry, self).save(*args, **kwargs)
    #
    #     # Store search content.
    #     self.update_search_index()
    #     return ret

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert a Person in the person table
# new_entry = Entry(title='title', slug='slug', content='content', published=True, timestamp=datetime.datetime.now())
# session.add(new_entry)
# session.commit()

print(session.query(Entry).first().timestamp)

