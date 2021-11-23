from flask import Flask, render_template, url_for, session, flash, redirect, request, jsonify
from mysql import connector
import mysql.connector
import Models.processFile
import Models.EditLevel
import Models.displayLevel
import Models.Dashboard
import telnetCom
import json
import operator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


# For Flash box in Processfile 
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Global Array 
mapList = []
LevelName = "Default"

# ---------------- APP ROUTES HERE -------------------------------------------- #
@app.route('/')
@app.route('/game')
def gamePlatform():

    print(Models.EditLevel.fetch_LastMapID())
    print(Models.EditLevel.fetchPassword())

    return render_template("index.html")

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
    return render_template("displayLevel.html", title="Level Display", output_data=data)


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


if __name__ == "__main__":
    # Error will be displayed on web page
    app.run(debug=True)

    

