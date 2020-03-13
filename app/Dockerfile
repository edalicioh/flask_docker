FROM python:3.7-alpine

MAINTAINER Edalicio Hazen "edalicio@outlook.com"

COPY . /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV AppConfig=/settings.cfg

VOLUME /app

ENTRYPOINT [ "python" ]
CMD ["./app.py"]