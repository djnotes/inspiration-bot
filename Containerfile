FROM docker.io/library/python:3.10

RUN pip3 install pyrogram tgcrypto apscheduler

COPY . /app

WORKDIR /app


CMD ["python","bot.py"]



