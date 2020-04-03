FROM python:rc-buster
RUN pip3 install flask sqlalchemy psycopg2

ADD . /app
WORKDIR /app

CMD python3 app.py
