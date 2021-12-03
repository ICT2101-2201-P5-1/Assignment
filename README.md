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

**CoolMotor.py**

![CoolMotor_1](https://user-images.githubusercontent.com/31657679/144558748-c2c37aa8-182d-4287-bf97-8bd86e2bd13c.png)
![CoolMotor_2](https://user-images.githubusercontent.com/31657679/144558766-61880dc4-48d4-4681-93b6-d52a274be7b3.png)
![CoolMotor_3](https://user-images.githubusercontent.com/31657679/144558782-aaa5e046-c9d5-4175-a4f1-6a899c94d66a.png)
![CoolMotor4](https://user-images.githubusercontent.com/31657679/144558797-e6ac8b01-5944-4003-aec8-a754b2e91987.png)
![CoolMotor5](https://user-images.githubusercontent.com/31657679/144558820-aa6496e5-4e3c-40cf-b49b-45b3f3083ce7.png)
![CoolMotor6](https://user-images.githubusercontent.com/31657679/144558831-6dc8db47-67fb-4168-a76a-65fd3ab54721.png)
![CoolMotor7](https://user-images.githubusercontent.com/31657679/144558846-5f1fb3b5-1afb-49b1-a0c0-e82c2069f437.png)
![CoolMotor8](https://user-images.githubusercontent.com/31657679/144558865-d0591d46-49b7-4127-bb9f-68e98747afc6.png)
![CoolMotor9](https://user-images.githubusercontent.com/31657679/144558883-0d377847-4c58-460e-9ba1-149aa9a35b0d.png)
![CoolMotor10](https://user-images.githubusercontent.com/31657679/144558903-d4b14608-5492-4e5f-91e4-4f6aab7109f8.png)
![CoolMotor11](https://user-images.githubusercontent.com/31657679/144558913-01562cc5-e9f1-4c33-8845-301061368692.png)


**DisplayLevel.py**

![displayLevel1](https://user-images.githubusercontent.com/31657679/144559169-b5533616-d5fc-4e2b-8050-0eafff6dbafe.png)
![displayLevel2](https://user-images.githubusercontent.com/31657679/144559191-fe05d691-814d-4b88-a3b6-15a0bf45db31.png)
![displayLevel3](https://user-images.githubusercontent.com/31657679/144559209-c6c47d02-9c64-451c-af07-6c2e7306ec14.png)

**EditLevel.py**

![editLevel1](https://user-images.githubusercontent.com/31657679/144559272-23639ce2-05ba-48b3-b25d-1e8d6c26ce68.png)
![editLevel2](https://user-images.githubusercontent.com/31657679/144559291-04844b77-d6ac-4419-adea-0bbae32d250c.png)

**ProcessFile.py**

![processFile1](https://user-images.githubusercontent.com/31657679/144559344-a7681b6c-b831-44f8-9462-d8d8752c9d66.png)
![processFile2](https://user-images.githubusercontent.com/31657679/144559359-8be47a19-e03b-4bf4-8131-f41ee3ffa58e.png)


**ProcessLogin.py**

![processLogin py](https://user-images.githubusercontent.com/31657679/144559397-5e579e2b-1d18-4f62-8db2-1e0967a73b74.png)


## Work Distribution & Plan

###### Updated Burndown Chart
![image](https://user-images.githubusercontent.com/31657679/144567504-57d61bbf-54ad-4cde-9ac8-d9e00c0eb25e.png)


###### Updated Gantt Chart
![image](https://user-images.githubusercontent.com/31657679/144568231-11edb329-285f-4811-bfe3-c04ebec34e1a.png)
![image](https://user-images.githubusercontent.com/31657679/144568267-0d12d93b-b285-45f6-9629-8cd053834ac1.png)


    
  
