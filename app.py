from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    key = os.environ.get("MY_KEY")
    if key:
        return f"Hello World {key}!"
    else:
        return "Hello World No Key"


if __name__ == "__main__":
    app.run(debug="True", host="0.0.0.0", port=5050)
