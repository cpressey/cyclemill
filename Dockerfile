FROM python:3.8.12-slim
RUN apt-get update && apt-get upgrade -y
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY website website
# CMD ["python", "-m", "http.server", "5000"]
WORKDIR /code/website
CMD ["python", "manage.py", "runserver", "5000"]
