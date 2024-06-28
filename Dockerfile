FROM python:3.10-slim
# Install the PostgreSQL development libraries
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
