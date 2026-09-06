from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def home():
    # Demonstrating simple output using Python 3.14
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    return f"<h1>Hello World!</h1><p>Your Python web app is running smoothly on version !! <b>{version}</b>.</p>"

if __name__ == "__main__":
    app.run()
