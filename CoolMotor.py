from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from mysql import connector
import mysql.connector
import Models.EditLevel
import telnetCom
import processFile
import json
import operator



app = Flask(__name__)

mapList = []
LevelName = "Default"

# ---------------- APP ROUTES HERE -------------------------------------------- #
@app.route('/')
@app.route('/game')
def gamePlatform():
    print(Models.EditLevel.fetchPassword())
    # To connect to car use these 2 methods 
    #telnetCom.sendCommands(b'drive')
    #telnetCom.receiveData()
    return render_template("index.html")


# LEVEL EDITOR
@app.route('/edit_level', methods=['GET', 'POST'])
def edit_level():
    if request.method == 'POST':
        jsdata = request.form['javascript_data'] 
        JSON_obj = json.loads(jsdata)  
        mapList.append(JSON_obj)
    mapList.sort(key=operator.itemgetter('position'))
    return render_template("LevelEditor/CreateLevel.html")


@app.route('/getMAPData', methods=['POST'])
def get_MAPData():
    if request.method == 'POST':
        CommandList = request.form.getlist('Commands')
        LevelName = request.form.get('LevelName')
        Difficulty = request.form.get('Difficulties')
        processFile.writeToMapFile(mapList,LevelName,CommandList, Difficulty)
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

    

