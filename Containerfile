FROM docker.io/library/alpine

RUN pip3 install apscheduler  PyMySQL

RUN pip3 install --pre SQLAlchemy

COPY . /app

WORKDIR /app


CMD ["python3","bot.py"]



