FROM python:3.12.2-alpine3.19

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN cp /app/bashrc /root/.bashrc
RUN pip install -r requirements.txt

RUN apk add --no-cache lsblk curl vim openssh-client busybox-extras htop mc openssl bash nmap arping tcpdump

EXPOSE 5000
CMD ["python", "/app/main.py"]
