from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('join.html')


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

@app.route('/start-game')
def start_game():
    return render_template('start_game.html')

@app.route('/auction')
def auction():
    return render_template('auction.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route("/result_page")
def result_page():
    return render_template("result_page.html")

