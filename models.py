from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Text, Float, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker

from datetime import datetime


ENGINE = create_engine('sqlite:///db.sqlite3', echo=True)
Base = declarative_base()

session = scoped_session(
    sessionmaker(
        bind = ENGINE,
        autocommit=False,
    )
)

class Token(Base):
    __tablename__ = 'tokens'

    _id = Column('id', Integer, primary_key = True)
    text = Column('token', Text)
    created_at = Column('created_at', DateTime)


Base.metadata.create_all(ENGINE)


if __name__=='__main__':
    token = Token()
    token.text = 'hello'
    token.created_at = datetime.utcnow()

    session.add(token)
    session.commit()
