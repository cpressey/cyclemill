FROM python:3.8.12-slim
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y wait-for-it
RUN apt-get install -y locales libcurl4-openssl-dev libssl-dev
WORKDIR /app/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 9808
COPY . .
ENTRYPOINT ["wait-for-it", "queue:5672", "--", "python", "./cli.py"]
