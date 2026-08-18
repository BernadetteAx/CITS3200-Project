from flask import Flask, render_template

app = Flask(__name__)

from app import routes

@app.route("/lobby")
def lobby():
    return render_template("lobby.html")