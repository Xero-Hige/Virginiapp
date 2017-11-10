import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

UNCLASIFIED = "-"


class TaggedTweet(Base):
    __tablename__ = "personas"

    id = Column(String, primary_key=True)
    date = Column(DateTime, primary_key=True)


import os
from sqlalchemy import create_engine

engine = create_engine(
        'postgres://kvxhqhxa:o1hwiW7SCsNNvN32z06pG6jDZJWbZeND@baasu.db.elephantsql.com:5432/kvxhqhxa')


from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind=engine)
try:
    Base.metadata.create_all(engine)
except:
    pass


class DB_Handler:
    def __init__(self):
        self.session = Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        self.session.close()

    def add(self, id):
        tweet = TaggedTweet(id=id, date=datetime.datetime.now())
        self.session.add(tweet)
        self.session.commit()

        return tweet
