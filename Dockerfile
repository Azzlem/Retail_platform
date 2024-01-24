FROM python:3.11

LABEL authors="MR.Sid.Alex"

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .