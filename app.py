
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Route for home page (serves index.html)
@app.route('/')
def home():
    return send_from_directory("my_site", "index.html")

# Route to serve all static files (HTML, CSS, JS)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory("my_site", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
