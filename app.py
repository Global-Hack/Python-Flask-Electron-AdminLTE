from __future__ import print_function
import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("/adminlte/index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5029)
