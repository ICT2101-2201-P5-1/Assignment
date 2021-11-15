from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from mysql import connector
import mysql.connector
import Models.EditLevel
import Models.Dashboard
import telnetCom

# For the chart
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     button = request.form.get('submit')
#
#     if(button):
#         print(button)
#         result = requests.get("http://192.168.10.105:80/"+button)
#         print("Result:"+ result)
#         if(result):
#             print("recieved ")
#     return render_template("index.html")

# ---------------- APP ROUTES HERE --------------------------------------------
@app.route('/')
@app.route('/game')
def gamePlatform():
    print(Models.EditLevel.fetchPassword())
    # To connect to car use these 2 methods 
    #telnetCom.sendCommands(b'drive')
    #telnetCom.receiveData()
    return render_template("index.html")



@app.route('/command', methods=['GET', 'POST'])
def command():
    if request.method == 'POST':
        command = request.form.get('command')
        print(command)
        commandB = bytes(command, 'utf-8')
        print(commandB)
        telnetCom.sendCommands(commandB)
    return render_template("command.html")

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # For the Charts
    # Bring some raw data.
    x1Array = []
    y1Array = []
    x2Array = []
    y2Array = []
    chart_data_1x = Models.Dashboard.fetchChart1x() #currently a tuple, remove the 2nd tuple then 
    chart_data_1y = Models.Dashboard.fetchChart1y() #currently a tuple, remove the 2nd tuple then 
    chart_data_2x = Models.Dashboard.fetchChart2x()
    chart_data_2y = Models.Dashboard.fetchChart2y()
    
    for first_x_tuple in chart_data_1x:
    	x1Array.append(first_x_tuple[0])
     
    for first_y_tuple in chart_data_1y:
    	y1Array.append(first_y_tuple[0])
     
    for second_x_tuple in chart_data_2x:
    	x2Array.append(second_x_tuple[0])

    for second_y_tuple in chart_data_2y:
    	y2Array.append(second_y_tuple[0])
    
    # print(x1Array)
    # print(y1Array)
    # # print(x2Array)
    # # print(y2Array)
    
    freq_series = pd.Series(y1Array)
    freq_series2 = pd.Series(y2Array)
    
    # Plot the figure.
    fig1 = plt.figure(figsize=(12, 8))
    ax = freq_series.plot(kind="bar")
    ax.set_title("Distance Travelled Per Game")
    ax.set_xlabel("Entry ID")
    ax.set_ylabel("Distance Travelled")
    ax.set_xticklabels(x1Array)
    plt.xticks(rotation=90)
    fig1.savefig('static/img/chart1.png')
    
    fig2 = plt.figure(figsize=(12, 8))
    ax = freq_series2.plot(kind="bar")
    ax.set_title("Time Played per day")
    ax.set_xlabel("Date of Play")
    ax.set_ylabel("Time Spent Playing")
    ax.set_xticklabels(x2Array)
    plt.xticks(rotation=90)
    fig2.savefig('static/img/chart2.png')
    
    # fig1 = plt.figure()
    # ax = fig1.add_axes([0,0,1,1])
    
    # # ax.bar(x1Array,y1Array)
    # ax.bar(x1Array,y1Array)
    # fig1.savefig('chart1.png')
    
    
    
    return render_template("dashboard.html", data=Models.Dashboard.fetchData())



if __name__ == "__main__":
    # Error will be displayed on web page
    app.run(debug=True)
    

