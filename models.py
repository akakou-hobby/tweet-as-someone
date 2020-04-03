from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Text, Float, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker

import secrets

import datetime

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

class Register():
    def __init__(self):
        pass

    def register(self):
        token = Token()

        token.token = secrets.token_urlsafe(32)
        
        token.created_at = datetime.datetime.utcnow()

        session.add(token)
        session.commit()

        return token

class Authenticater():
    def __init__(self, token):
        self.token = token
        self.hit = None
        self.result = False

    def auth(self):
        now = datetime.datetime.utcnow()

        delta = datetime.timedelta(minutes=15)
        allowed = now - delta

        hits = session.query(Token).\
            filter(Token.token == self.token, Token.created_at >= allowed).\
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
    register = Register()
    token = register.register()

    auth = Authenticater(token.token)
    print('result:', auth.auth())
    auth.destroy()

    auth = Authenticater(token.token)
    print('result:', auth.auth())
    auth.destroy()

