FROM python:rc-buster
RUN pip3 install flask sqlalchemy

ADD . /app
WORKDIR /app

CMD python3 app.py
