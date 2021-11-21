from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from mysql import connector
import mysql.connector
import Models.EditLevel
import Models.Dashboard
import telnetCom

# For the chart
from matplotlib import pyplot as plt
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

'''
dashboard() function is to create the charts and call the dashboard.html view model

    @param x1Array            Empty list is initialised for 1st chart's x-axis
    @param y1Array            Empty list is initialised for 1st chart's y-axis
    @param x2Array            Empty list is initialised for 2nd chart's x-axis
    @param y2Array            Empty list is initialised for 2nd chart's y-axis
    
    @param chart_data_1x      Call Dashboard.py controller function which is an SQL query to call the 1st chart's x-axis
    @param chart_data_1y      Call Dashboard.py controller function which is an SQL query to call the 1st chart's y-axis
    @param chart_data_2x      Call Dashboard.py controller function which is an SQL query to call the 2nd chart's x-axis
    @param chart_data_2y      Call Dashboard.py controller function which is an SQL query to call the 2nd chart's y-axis
    
    Originally, fetched SQL data is a tuple and unuseable by matplotlib. It is changed to a list.
    
    @param freq_series        Uses pandas to initialise the y-axis of the 1st chart
    @param freq_series2       Uses pandas to initialise the y-axis of the 2nd chart
    
    @param fig1               Initialises the 1st chart
    @param ax                 Initialises how the data is reperesented by the 1st chart
    @param ax.set_title       Sets the Title of the chart
    @param ax.set_xlabel      Labels the x-axis of the 1st chart
    @param ax.set_ylabel      Labels the y-axis of the 1st chart
    @param ax.set_xticklabels Initiaises the x-axis of the 1st chart
    @param plt.xticks         Formats the x-axis' labels of the 1st chart
    @param plt.yticks         Formats the y-axis' labels of the 1st chart
    @param fig1.savefig       Saves the 1st chart for displaying by the view model
    
    @param fig2               Initialises the @nd chart
    @param ax                 Initialises how the data is reperesented by the 1st chart
    @param ax.set_title       Sets the Title of the chart
    @param ax.set_xlabel      Labels the x-axis of the 2nd chart
    @param ax.set_ylabel      Labels the y-axis of the 2nd chart
    @param ax.set_xticklabels Initiaises the x-axis of the 2nd chart
    @param plt.xticks         Formats the x-axis' labels of the 2nd chart
    @param plt.yticks         Formats the y-axis' labels of the 2nd chart
    @param fig2.savefig       Saves the 2nd chart for displaying by the view model
    
    @return                   Displays the dashboard onto the dashboard.html view model. 
                              Also, data, which is passed into the return, takes in an SQL query from the model Dashboard.py to display data 
'''

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    
    x1Array = []
    y1Array = []
    x2Array = []
    y2Array = []
    
    chart_data_1x = Models.Dashboard.fetchChart1x() 
    chart_data_1y = Models.Dashboard.fetchChart1y()
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
    
    freq_series = pd.Series(y1Array)
    freq_series2 = pd.Series(y2Array)
    
    fig1 = plt.figure(figsize=(12, 8))
    ax = freq_series.plot(kind="bar")
    ax.set_title("Distance Travelled Per Game", fontsize=25)
    ax.set_xlabel("Entry ID", fontsize=20)
    ax.set_ylabel("Distance Travelled", fontsize=20, rotation=90)
    ax.set_xticklabels(x1Array)
    plt.xticks(fontsize=16, rotation=0)
    plt.yticks(fontsize=16, rotation=0)
    fig1.savefig('static/img/chart1.png')
    
    fig2 = plt.figure(figsize=(12, 8))
    ax = freq_series2.plot(kind="bar")
    ax.set_title("Time Played per day", fontsize=25)
    ax.set_xlabel("Date of Play", fontsize=20)
    ax.set_ylabel("Time Spent Playing", fontsize=20, rotation=90)
    ax.set_xticklabels(x2Array)
    plt.xticks(fontsize=16, rotation=0)
    plt.yticks(fontsize=16, rotation=0)
    fig2.savefig('static/img/chart2.png')

    return render_template("dashboard.html", data=Models.Dashboard.fetchData())

if __name__ == "__main__":
    # Error will be displayed on web page
    app.run(debug=True)
    

