from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def main_func():
    content = "<p>el pepe ete sech</p>"
    return content

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()