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
    if request.method == 'GET':
        CommandList = request.args.getlist('Commands')
        LevelName = request.args.get('LevelName')
        Difficulty = request.args.get('Difficulties')
        processFile.writeToMapFile(mapList,LevelName,CommandList, Difficulty)
        mapList.clear()
    return render_template("LevelEditor/CreateLevel.html")


@app.route('/command', methods=['GET', 'POST'])
def command():
    if request.method == 'POST':
        command = request.form.get('command')
        print(command)
        commandB = bytes(command, 'utf-8')
        print(commandB)
        telnetCom.sendCommands(commandB)
    return render_template("command.html")



if __name__ == "__main__":
    # Error will be displayed on web page
    app.run(debug=True)

    

