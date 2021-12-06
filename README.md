# CoolMotor
ICT 2101/2201 Team Project P5-1

Project Board: https://github.com/orgs/ICT2101-2201-P5-1/projects/1

Team Leader: May Madi Aung - @mayinot (2002390) **Code Reviewer 1**

Member: Tan Chu Qing Alicia - @BestCrochet (2001874) **Code Reviewer 2**

Member: Shawn Lemuel Evora Dabi - @ShawnLemuelDabi (2001401)

Member: Woo Kah Howe - @JustAyce (2001138)

Member: Tudyisster Siva - @WeirdBalls (2002131)
## Install 
Install these dependencies before running:
    
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
Navigate to 127.0.0.1:5000.
    
### Necessary dependencies
- Flask
- Flask-Bcrypt
- Flask-MySQLdb
- Flask-WTF 

## Development Workflow
The team will be using **Feature branching** Git Workflow. Each member will branch out from Dev to work on their assigned Features, as stated below. 

After each feature is finailized, members will do PR to the Dev Branch. All PR to Dev will be reviewed by Code Reviewers (May or Alicia). Upon approval, the Code Reviewer will merge the feature to Dev. Each Feature branch should be named ```feature/<name of feature>```.

Another way members can make changes to Dev will be through Hot-Fixes. Hot-Fixes should only be done if there is a bug inside the Dev branch. The naming convention for the Hot-Fix branch will be ```Hot_Fix-<name of error>```.
    
**Feature Work Distribution:**
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
<<<<<<< HEAD
  - Store game data to db (Shawn)
=======
  - Store game data to db (Alicia)
>>>>>>> master
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

**Testing Work Distribution**
- White Box Testing 
    - CoolMotor.py (edit_level, get_MAPData, view_display_Level, delete_level and login) (Tudy)
    - DisplayLevel.py (Tudy)
    - EditLevel.py (Shawn)
    - ProcessFile.py (May)
    - ProcesLogin.py (Alicia)
    - WBT Video (Shawn)
- Black Box Testing (Kah Howe)
    - UAT Video (Kah Howe)
    
## Black Box Testing (UAT)
For User Acceptance Testing, the team will be covering all test cases documented in our original M2, under section **6.4 Test Case**. The test cases are labelled on the top right hand corner of the video. 

Video Link: https://youtu.be/jya3VeKFCvQ 
(not embedded as the file size is too big)

## Whitebox Testing
The team has chosen the Level Management control class for white box testing. This control class encompasses the Level Editor feature and includes the Administrator Login, Creating new levels, Viewing Levels and Deleting Levels. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/66672755/144711437-a2bf3145-953e-417d-95d5-8541478adfca.png" alt="Level Management Controller Class"/>
</p>
    
#### Functions and Files Tested
    
Controller: ```CoolMotor.py``` (```edit_level()```, ```get_MAPData()```, ```view_display_Level()```, ```delete_level()``` and ```login()```)

Models: ```displayLevel.py```, ```editLevel.py```, ```processFile.py``` and ```processLogin.py```
    
#### Test Codes (unittest — Unit testing framework)
The team used ```unittest```(https://docs.python.org/3/library/unittest.html) to test our code. In addition, the team also set up a test database to test our model classes. The credentials of our test database is specified in Credentials\constants.py, below the credentials of our real database. 
    
     $ py -m unittest //Remember to run all flask environment before running the test cases

19 test cases were ran in total.
<p align="center">
  <img src="https://user-images.githubusercontent.com/31657679/144563838-bb9a157b-e508-4727-9281-bca997189c9b.png" alt="Test Cases"/>
</p>

**Test Codes Files:**
- test_CoolMotor.py
- test_displayLevel.py
- test_EditLevel.py
- test_processFile.py
- test_processLogin.py
- constants.py
     
## Unit Test Statistics 

#### Statement Coverage | Coverage.py
The team will also be using ```Coverage.py```(https://coverage.readthedocs.io/en/6.2/) to measure the coverage of our test cases. We chose Coverage.py as it can be tested together with unittest.

Generating the coverage report:

     $ coverage run -m unittest discover
     $ coverage html
     
     
As mentioned aboved, the team managed to cover 100% on Level Editor Feature Tested; CoolMotor.py (edit_level, get_MAPData, view_display_Level, delete_level and login), DisplayLevel.py, EditLevel.py, ProcessFile.py and ProcesLogin.py. The full coverage HTML reports can be found inside the repository at ```Testing/Coverage/```.

<p align="center">
  <img src="https://user-images.githubusercontent.com/31657679/144564167-aa00ba83-0bac-4224-8d9b-3344309bd4a4.png" alt="Coverage"/>
</p>

White Box Testing Video: 

https://user-images.githubusercontent.com/66672755/144710750-93c3d722-9e29-4751-bd31-20facfd833fe.mp4


#### Control Flow Graphs (CFG)

All CFGs can be found at https://github.com/ICT2101-2201-P5-1/CoolMotor/wiki!    (it was too long so we put them there)

## Work Distribution & Plan
#### Updated Burndown Chart
<p align="center">
  <img src="https://user-images.githubusercontent.com/31657679/144567504-57d61bbf-54ad-4cde-9ac8-d9e00c0eb25e.png" alt="Burndown Chart"/>
</p>

#### Updated Gantt Chart

<p align="center">
  <img src="https://user-images.githubusercontent.com/31657679/144568231-11edb329-285f-4811-bfe3-c04ebec34e1a.png" alt="Coverage"/>
    <img src="https://user-images.githubusercontent.com/31657679/144568267-0d12d93b-b285-45f6-9629-8cd053834ac1.png" alt="Coverage"/>
</p>


    
  
