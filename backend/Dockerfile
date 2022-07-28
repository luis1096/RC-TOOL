FROM python:alpine

WORKDIR /usr/src/backend
COPY . .

RUN apk update && apk upgrade && pip3 install -r requirements.txt
CMD python wsgi.py