from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from mysql import connector
import mysql.connector
import Models.processFile
import Models.EditLevel
import telnetCom
import json
import operator



app = Flask(__name__)

# Global Array 
mapList = []
LevelName = "Default"

# ---------------- APP ROUTES HERE -------------------------------------------- #
@app.route('/')
@app.route('/game')
def gamePlatform():
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
        Models.processFile.writeToMapFile(mapList,LevelName,CommandList, Difficulty)
        # Clear the array after every submission 
        mapList.clear()
    return render_template("LevelEditor/CreateLevel.html")





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


if __name__ == "__main__":
    # Error will be displayed on web page
    app.run(debug=True)

    

