FROM python:3.7-alpine

MAINTAINER Edalicio Hazen "edalicio@outlook.com"

COPY . .
WORKDIR /app

COPY /app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ENV AppConfig=/app/settings.cfg

VOLUME /app

ENTRYPOINT [ "python" ]
CMD ["/run.py"]