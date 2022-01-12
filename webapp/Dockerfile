FROM python:3.8.12-slim
RUN apt-get update && apt-get upgrade -y
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
WORKDIR /code/webapp
CMD ["bash", "startup.sh"]
