FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]