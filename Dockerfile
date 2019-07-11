FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DOCKER_DB 1

RUN mkdir /app
WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN apk update && apk add --no-cache --virtual build-deps \
    gcc \
    python3-dev \
    && apk add --no-cache musl-dev \
    postgresql-dev \
    && pipenv install --system --dev --deploy \
    && apk del --no-cache build-deps

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
