#!flask/bin/python

import connexion
from flask_cors import CORS
from flask import Flask, request, render_template

app = Flask(__name__)

CORS(app)

@app.route("/<id>")
def home(id):
    return render_template("index.html")
