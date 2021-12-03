# CoolMotor
ICT 2101/2201 Team Project P5-1


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
- Testing 
    - CoolMotor.py (edit_level, get_MAPData, view_display_Level, delete_level and login) (Tudy)
    - DisplayLevel.py (Tudy)
    - EditLevel.py (Shawn)
    - ProcessFile.py (May)
    - ProcesLogin.py (Alicia)
    - UAT Video (Kah Howe)
    - WBT Video (Shawn)


## UAT
For User Acceptance Testing, the team will be covering all test cases covered in M2 under section **6.4 Test Case**. The video label each test case with #TC_Number on the upper right hand of the video. Here is a quick run through of all UAT cases  **<add video here!>  **   


## Whitebox Testing
The team have chosen Level Editor Feature as the meaningful classes, we will be using to demonstrate our test code. Level Editor include Administrator Login, Creating new levels, Viewing Levels and Deleting Levels. 
    
###### Level Editor Feature Tested
    
    Control: CoolMotor.py (edit_level, get_MAPData, view_display_Level, delete_level and login) 
    Models: DisplayLevel.py, EditLevel.py, ProcessFile.py and ProcesLogin.py 
    
    
###### Test Codes (unittest — Unit testing framework)
The team used unittest to test our code. We are able to assert into our codes using unittest. In addition, the team set up a test database to test our model classes. The credentials of our test database is specified in Credentials\constants.py below the credentials of our real database. 

![image](https://user-images.githubusercontent.com/31657679/144563838-bb9a157b-e508-4727-9281-bca997189c9b.png)
    
     $ py -m unittest //Remember to run all flask environment before running the test cases
     
**Test Codes Files:**
- test_CoolMotor.py
- test_displayLevel.py
- test_EditLevel.py
- test_processFile.py
- test_processLogin.py
- constants.py


     
     
## Unit Test Statistics 

###### Statement Coverage | Coverage.py
The team will also be using Coverage.py to measure the coverage we manage to cover with our test cases. We chose Coverage.py as it can be tested together with unittest. The video of the team running Test Case Coverage is attached below. 

     $ coverage run -m unittest discover
     $ coverage html
     
     
As mentioned aboved, the team managed to cover 100% on Level Editor Feature Tested; CoolMotor.py (edit_level, get_MAPData, view_display_Level, delete_level and login), DisplayLevel.py, EditLevel.py, ProcessFile.py and ProcesLogin.py.

![image](https://user-images.githubusercontent.com/31657679/144564167-aa00ba83-0bac-4224-8d9b-3344309bd4a4.png)

We have ran the test cases and attached the video **<add video here!>  **   

###### Branch Coverage | Control Flow Graph (CFG)

All CFGs can be found at https://github.com/ICT2101-2201-P5-1/CoolMotor/wiki!(it was too long so we put them there)

## Work Distribution & Plan

###### Updated Burndown Chart
![image](https://user-images.githubusercontent.com/31657679/144567504-57d61bbf-54ad-4cde-9ac8-d9e00c0eb25e.png)


###### Updated Gantt Chart
![image](https://user-images.githubusercontent.com/31657679/144568231-11edb329-285f-4811-bfe3-c04ebec34e1a.png)
![image](https://user-images.githubusercontent.com/31657679/144568267-0d12d93b-b285-45f6-9629-8cd053834ac1.png)


    
  
