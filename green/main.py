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
def hello():

    return "🟩 green service host: "+socket.gethostname()+"\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

