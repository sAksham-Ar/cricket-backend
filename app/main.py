from flask import Flask
from criapi import Cricbuzz
import json

app=Flask(__name__)
c=Cricbuzz()

@app.route("/")
def home():
    return "The server is live!"

@app.route("/matches")
def matches():
    return json.dumps(c.livescore())

@app.route("/commentary/<id>")
def commentary(id):
    return json.dumps(c.commentary(id))


@app.route("/scorecard/<id>")
def scorecard(id):
    return json.dumps(c.scorecard(id))

