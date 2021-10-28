FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /schedule
WORKDIR /schedule
ADD requirements.txt /schedule/
RUN pip install -r requirements.txt
ADD . /schedule/