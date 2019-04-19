from flask import Flask

app = Flask(__name__)

@app.route("/add")
def hello():
    return "Hello Flask, on Azure App Service for Linux"