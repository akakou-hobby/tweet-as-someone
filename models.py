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
    token = Column('token', Text)
    created_at = Column('created_at', DateTime)


class Authenticater():
    def __init__(self, token):
        self.token = token
        self.hit = None
        self.result = False

    def auth(self):
        hits = session.query(Token).\
            filter(Token.token == self.token).\
            all()

        print(hits)
        
        self.result = bool(hits)
        if self.result:
            self.hit = hits[0]

        return self.result

    def destroy(self):
        if self.result:
            session.query(Token).\
                filter(Token._id == self.hit._id).\
                delete()
        
        session.commit()


Base.metadata.create_all(ENGINE)


if __name__=='__main__':
    token = Token()
    token.token = 'hello'
    token.created_at = datetime.utcnow()

    session.add(token)
    session.commit()

    auth = Authenticater('good morning')
    print('result:', auth.auth())
    auth.destroy()

    auth = Authenticater('hello')
    print('result:', auth.auth())
    auth.destroy()

    auth = Authenticater('hello')
    print('result:', auth.auth())
    auth.destroy()
