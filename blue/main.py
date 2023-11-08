import socket
import math
from flask import Flask
from threading import Thread
app = Flask(__name__)

#docker build --tag openterprise/blue:latest .
#docker push openterprise/blue:latest

def generate_load():
    x = 0.0001
    for i in range(0,1000):
        x += math.sqrt(x)


@app.route("/")
@app.route("/blue")
@app.route("/blue/")
def hello():

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return "🟦 blue container hostname: {}, container IP: {}\n".format(hostname,ip_address)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

