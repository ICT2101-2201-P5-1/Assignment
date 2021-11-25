from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, session
from mysql import connector
import mysql.connector
import Models.EditLevel
import telnetCom
from Models.processLogin import LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

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
    #telnetCom.sendCommands(b'hello')
    #telnetCom.receiveData()
    session['attempt'] = 5
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    form.load()
    if form.check():
        redirect(url_for('gamePlatform'))
    else:
        form.load()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    # Error will be displayed on web page
    app.run(debug=True)
    

