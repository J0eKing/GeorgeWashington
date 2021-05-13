from flask import Flask
from threading import Thread

app = Flask('asdasd')


@app.route('/')
def home():
    return "I'm alive"


def run():
    print("start server")
    app.run(host='0.0.0.0', port=6666)


def keep_alive():
    t = Thread(target=run)
    t.start()
