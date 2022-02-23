import os

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def test():
    return render_template("index.html")


@app.route("/forMom")
def mom_invite():
    return render_template("index-mom.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
