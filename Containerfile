FROM python:3

RUN pip3 install pyrogram tgcrypto apscheduler

COPY . /app

WORKDIR /app


CMD ["python","bot.py"]



