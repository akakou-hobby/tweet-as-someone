FROM python:rc-buster
RUN pip3 install flask sqlalchemy psycopg2 tweepy

ADD . /app
WORKDIR /app

CMD python3 app.py
