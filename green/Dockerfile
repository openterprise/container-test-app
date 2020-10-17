FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

RUN apk update
RUN apk add lsblk

EXPOSE 5000
CMD ["python", "/app/main.py"]
