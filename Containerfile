FROM ghcr.io/djnotes/pyrogram-image:latest

RUN pip install apscheduler  PyMySQL

RUN pip install --pre SQLAlchemy

COPY . /app

WORKDIR /app


CMD ["python3","bot.py"]



