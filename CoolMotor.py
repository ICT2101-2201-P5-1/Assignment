from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, make_response,session
from mysql import connector
import mysql.connector
import Models.processFile
import Models.EditLevel
import Models.GamePlatform
import Models.displayLevel
import Models.Dashboard
import telnetCom
from Models.processLogin import LoginForm
import json
import operator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# For Flash box in Processfile 
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Global Array 
mapList = []
LevelName = "Default"

# ---------------- APP ROUTES HERE --------------------------------------------
@app.route('/', methods=['GET','POST'])
def gamePlatform():
    # To connect to car use these 2 methods 
    #telnetCom.sendCommands(b'hello')
    #telnetCom.receiveData()
    # win game scenario call-back
    levelsData = Models.displayLevel.display()
    if request.method == "POST":
        # check for lastLevelLoaded, set variable = 1 (tutorial level) if unset
        win = request.get_json().get('win')
        map_id = request.get_json().get('map_id')
        map_difficulty = request.get_json().get('map_difficulty')
        game_min = request.get_json().get('game_minutes')
        game_sec = request.get_json().get('game_seconds')
        dist_travelled = request.get_json().get('dist_travelled')
        if win == 1:
            total_secs = int(game_min) * 60 + int(game_sec)
            # store data to db
            Models.GamePlatform.storeGameDataToDB(map_id, map_difficulty, dist_travelled, total_secs)
            pass

    lll = 1
    if request.cookies.get('lastLevelLoaded') is not None:
        lll = request.cookies.get('lastLevelLoaded')

    mapId, mapDifficulty, mapName, mapFile = Models.GamePlatform.readMapDataFromDB(lll)
    commandList, mapData = Models.GamePlatform.initLevelLayout(mapFile)

    return render_template("index.html"
                           , mapLevelLayout=mapData
                           , commandList=commandList
                           , mapName=mapName
                           , mapId=mapId
                           , mapDifficulty=mapDifficulty
                           ,levelsData=levelsData)


# set last level loaded as cookie..
@app.route('/selectLevel' , methods=['GET','POST'])
def selectLevel():

    res = make_response(redirect(url_for('gamePlatform')))

    if request.method == "POST":
        # check for lastLevelLoaded, set variable = 1 (tutorial level) if unset
        if not request.cookies.get('lastLevelLoaded'):
            res.set_cookie('lastLevelLoaded', '1', max_age=60 * 60 * 24 * 365 * 2)

        else:
            mid = request.form.get('level')
            print(mid)
            res.set_cookie('lastLevelLoaded', mid, max_age=60 * 60 * 24 * 365 * 2)
            
    return res


'''
Edit Level
    Handle receiving of POST request from Map and rendering of CreateLevel page 
        @param jsdata The data transfered from drag & drop interface 
        @param JSON_obj JSON object in position: "2", value:"goal"
        @param mapList global array 
        @return the CreateLevel.html page 
'''
@app.route('/edit_level', methods=['GET', 'POST'])
def edit_level():
    # Get post request from TranserJson(value,data) JS
    if request.method == 'POST':
        jsdata = request.form['javascript_data'] 
        JSON_obj = json.loads(jsdata)  
        # convert JSON string to mapList 
        mapList.append(JSON_obj)
    # sort list 
    mapList.sort(key=operator.itemgetter('position'))
    return render_template("LevelEditor/CreateLevel.html")


'''
    Get Map Data 
        Handle receiving of POST request from Level_Editor_Form and rendering of CreateLevel page 
            @param CommandList The id list of checked commands
            @param LevelName String levelName user input
            @param Difficulty value 1(easy),2(medium),3(hard)
            @return the CreateLevel.html page 
'''
@app.route('/getMAPData', methods=['POST'])
def get_MAPData():
    # Get post request from form when user submit
    if request.method == 'POST':
        CommandList = request.form.getlist('Commands')
        LevelName = request.form.get('LevelName')
        Difficulty = request.form.get('Difficulties')
        status = Models.processFile.writeToMapFile(mapList,LevelName,CommandList, Difficulty)
        # Clear the array after every submission 
        mapList.clear()
        if status == 'success':
            flash("Level created successsfully!")
        else:
            flash("Please select a goal in the map!")
            redirect(url_for('edit_level'))
      
    return render_template("LevelEditor/CreateLevel.html")

'''
This routes to the displaylevel.html, that page will display
all the levels stored in the database and allow for deletes. 
'''
@app.route("/displayLevel")
def view_display_Level():
    data = Models.displayLevel.display()
    return render_template("LevelEditor/displayLevel.html", title="Level Display", output_data=data)


'''
This route takes the variable passed by the delete button 
in the displaylevel.html and passes it to the delete function
        @param id           Is the variable that it receives from the displaylevel.html delete button
'''
@app.route("/deletelevel/<int:id>", methods=['POST'])
def delete_level(id):
    Models.displayLevel.delete(id)
    session.pop('_flashes', None)
    flash('Deletion Successful', "info")
    return redirect(url_for('view_display_Level'))



#-----------------------------May Communication Testing--------------------------------------------------------------#
@app.route('/command', methods=['GET', 'POST'])
def command():
    if request.method == 'POST':
        command = request.form.get('command')
        print(command)
        commandB = bytes(command, 'utf-8')
        print(commandB)
        telnetCom.sendCommands(commandB)
    return render_template("command.html")

@app.route('/getCarData', methods=['POST'])
def get_data():
    Car_data = telnetCom.receiveData()
    print(Car_data)
    return render_template("command.html", Car_data=Car_data)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    Models.Dashboard.getGameDataFromDB()
    return render_template("dashboard.html", data=Models.Dashboard.fetchData())



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    form.load()
    ## keep output in var change 
    if form.check() == "Success":
        flash('Login Successful', "info")
        return redirect(url_for('edit_level'))
    elif form.check() == "Fail":
        form.load()
        flash('Wrong Password!')
        
    elif form.check() == "Timeout":
        form.load()
        flash('Too many incorrect logins incident!')
    
    return render_template('LevelEditor/login.html', title='Login', form=form)



if __name__ == "__main__":
    # Error will be displayed on web page
    app.run(debug=True)


