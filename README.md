# CoolMotor
ICT 2101/2201 Team Project P5-1

Development Workflow:

Team Leader: May Madi Aung - @mayinot (2002390) **Code Reviewer 1**

Member: Tan Chu Qing Alicia - @BestCrochet (2001874) **Code Reviewer 2**

Member: Shawn Lemuel Evora Dabi - @ShawnLemuelDabi (2001401)

Member: Woo Kah Howe - @JustAyce (2001138)

Member: Tudyisster Siva - @WeirdBalls (2002131)
## Install 
Install these dependency before running 
    
    $ pip install Flask 
    $ pip install mysql-connector-python
    $ pip install MySql
    $ pip install matplotlib
    $ pip install pandas 
    $ pip install -U Flask-WTF
    $ pip install flask-bcrypt
    

## How to Run
The web interface uses the flask framework. To start the web portal, run the following:
    
    set flask_app=CoolMotor
    flask run
## Development Workflow
The team will using **Feature branching** Git Workflow. Each member will branch out from Dev to work on their assigned Features, as stated below. After each feature is finailized, members will do PR to Dev Branch. All PR to Dev will be review by Code Reviews. Upon approval, Code Review will merge feature to Dev. Each Feauture branch should be name feature/name of feature.

Another way members can make changes to Dev will be thtrough Hot-Fix. Hot-Fix should only be done if member find major error in Dev. Naming convention of Hot-Fix will be Hot_Fix-Name of Error
    
**Features Members are assigned:**
- Database and Page setup (Shawn)
- Game Platform
  - Drag-and-drop interface integration (Alicia)
  - Virtual grid map (Alicia)
  - Game Logic Processing: Parse and process commands & Send commands (Alicia)
  - Game Logic Processing: Car crashes scenarios 1 & 2 (Alicia)
  - Game Logic Processing: Collect coin scenario (Alicia)
  - Game Logic Processing: Win game scenario (Alicia) 
   - Car detects obstacles (Shawn)
  - Game Logic Processing: Render map, objects (Alicia)
  - Store game data to db (Alicia)
  - Select / Change Levels (May)
  - Live Dashboard (Shawn)
- Level Editor
  - Login Page (Kah Howe)
   - Login verification & session (Kah Howe)
   - Bruteforce checker (Kah Howe)
  -  Create Levels (May)
    - Virtual grid map (May)
    - Process file (May)
    - Save level data to db (May)
  -  View list of levels (Tudy)
    - Delete Levels (Tudy)
- Dashboard
  - Load level data from DB (Shawn)
  - Graph statistics 1 (Shawn)
  - Graph statistics 2 (Shawn)
- Physical Car
    - Send Commands to Car (May)
    - Recieve Commands from Car (Shawn)


## UAT

## Whitebox Testing
The team have chosen Level Editor Feature as the meaningful classes, we will be using to demonstrate our test code. Level Editor include Administrator Login, Creating new levels, Viewing Levels and Deleting Levels. 
    
###### Level Editor Feature Tested
    
    Control: CoolMotor.py ( edit_level, get_MAPData, view_display_Level, delete_level and login) 
    Models: DisplayLevel.py, EditLevel.py, ProcessFile.py and ProcesLogin.py 
    
    
###### Test Codes (unittest — Unit testing framework)
The team used unittest to test our code. We are able to assert into our codes using unittest. In addition, the team set up a test database to test our model classes. The credentials of our test database is specified in Credentials\constants.py below the credentials of our real database. The team will also be using Coverage.py to measure the coverage we manage to cover with our test cases. We chose Coverage.py as it can be tested together with unittest. 
    
     $ py -m unittest
    
    
    
    
  
