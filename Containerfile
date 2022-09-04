FROM ghcr.io/djnotes/pyrogram-image:latest

RUN pip3 install pyrogram tgcrypto apscheduler SQLAlchemy PyMySQL

COPY . /app

WORKDIR /app


CMD ["python","bot.py"]



