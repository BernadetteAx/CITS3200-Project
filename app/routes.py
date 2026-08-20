from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('home_page.html')


@app.route('/host')
def host():
    return render_template('host_game_page.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/instructions')
def instructions():
    return render_template('instructions_page.html')

@app.route("/lobby")
def lobby():
    return render_template("lobby.html")

@app.route('/auction')
def auction():
    return render_template('auction.html')




# This html page is just for testing and is temporary
@app.route('/mission')
def mission():
    return render_template('test-mission.html')