import socket
import math
from flask import Flask
from threading import Thread
app = Flask(__name__)

#docker build --tag openterprise/green:latest .
#docker push openterprise/green:latest

def generate_load():
    x = 0.0001
    for i in range(0,1000):
        x += math.sqrt(x)


@app.route("/")
@app.route("/green")
@app.route("/green/")
@app.route("/healthz")
@app.route("/healthz/")
@app.route("/healthz/live")
@app.route("/healthz/ready")
def hello():

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return "🟩 green container hostname: {}, container IP: {}\n".format(hostname,ip_address)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

