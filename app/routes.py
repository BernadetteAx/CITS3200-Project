from flask import render_template
from app import app
from app.game_data.mission_structs import missions_list
from app.game_data.location_info import location_info


@app.context_processor
def visual_catalog():
    return {"game_visual_catalog": {
        "missions": [{"name": mission["mission_name"], "locations": mission["location_options"]}
                     for mission in missions_list],
        "targets": {location: {"artifact": info["artifact_to_steal"], "jewel": info["jewel_to_steal"]}
                    for location, info in location_info.items()},
    }}

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

@app.route('/start_game')
def start_game():
    return render_template('start_game.html')

@app.route('/mission_description')
def mission_description():
    return render_template('mission_description.html')

@app.route('/auction')
def auction():
    return render_template('auction.html')




# This html page is just for testing and is temporary
@app.route('/test_mission')
def test_mission():
    return render_template('test-mission.html')
  
@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route("/result_page")
def result_page():
    return render_template("result_page.html")

