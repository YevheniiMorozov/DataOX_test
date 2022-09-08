FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /user/src/app/requirements.txt

WORKDIR /usr/src/app

RUN pip install -r requirements.txt
