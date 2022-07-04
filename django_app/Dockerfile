FROM python:3.9-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt  

EXPOSE 8000
