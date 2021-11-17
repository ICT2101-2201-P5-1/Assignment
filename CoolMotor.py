from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, make_response
from mysql import connector
import mysql.connector
import Models.EditLevel
import Models.GamePlatform
import telnetCom




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
def gamePlatform():
    # To connect to car use these 2 methods 
    #telnetCom.sendCommands(b'hello')
    #telnetCom.receiveData()

    lll = 1
    if request.cookies.get('lastLevelLoaded') is not None:
        lll = request.cookied.get('lastLevelLoaded')

    mapFile = Models.GamePlatform.readMapDataFromDB(lll)
    Models.GamePlatform.initLevelLayout("Levels/1.txt")

    return render_template("index.html")

# set last level loaded as cookie..
@app.route('/set-level')
def selectLevel():

    res = make_response("Set last level loaded as cookie")

    if request.method == "POST":
        # check for lastLevelLoaded, set variable = 1 (tutorial level) if unset
        if not request.cookies.get('lastLevelLoaded'):
            res.set_cookie('lastLevelLoaded', '1', max_age=60 * 60 * 24 * 365 * 2)

        else:
            mid = request.form.get('level')
            res.set_cookie('lastLevelLoaded', mid, max_age=60 * 60 * 24 * 365 * 2)

    return res



if __name__ == "__main__":
    # Error will be displayed on web page
    app.run(debug=True)


