FROM python:3.9-alpine

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

RUN apk add --no-cache lsblk curl vim openssh-client busybox-extras htop mc openssl

EXPOSE 5000
CMD ["python", "/app/main.py"]
