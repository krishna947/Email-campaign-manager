FROM python:3.10

WORKDIR /myapp

RUN apt-get update

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD "bash"
