FROM python:3.8.12-slim
RUN apt-get update && apt-get upgrade -y
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "manage.py", "runserver"]
