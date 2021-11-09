from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from mysql import connector
import mysql.connector
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
@app.route('/game')
def gamePlatform():
    #telnetCom.sendCommands(b'hello')
    #telnetCom.receiveData()
    return render_template("index.html")

if __name__ == "__main__":
    # Error will be displayed on web page
    app.run(debug=True)
    

