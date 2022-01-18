FROM python:3.8.12-slim
# FROM python:3.9.1

EXPOSE 9808

WORKDIR /app/

RUN pip install poetry==1.1.4
COPY pyproject.toml poetry.lock /app/
RUN apt-get update && \
    apt-get install -y locales libcurl4-openssl-dev libssl-dev git gcc && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction #!COMMIT && \
    apt-get remove -y gcc git && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1

COPY . /app/

ENTRYPOINT ["python", "/app/cli.py"]
