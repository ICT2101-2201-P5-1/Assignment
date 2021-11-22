import Models.EditLevel


'''
Write To Map File
    Handle the file processing validate if the dictionary have Goal sprite if 
    Goal sprite is present insert new Level Map into a text file under levels folder 
    and call on Model to insert to database.
        @param CommandList The id list of checked commands
        @param LevelName String levelName user input
        @param Difficulty value 1(easy),2(medium),3(hard)
        @param mapList Array that store position and sprite
        @param MapDict (Position: Sprite) key and value pair 
        @param fileName is path to generate new textfile
        @param dbfilePath used to change formating of level map (coordinate with map rendering)
        @param fileObj file object
        @param dbStatus status of insert statement (sucess/fail)
        @return success/fail
'''
def writeToMapFile(Maparray,LevelName,CommandList, Difficulty):
    MapDict ={}
    for grid in Maparray:
        MapDict[grid['position']]= grid['type']
    if 'goal' in MapDict.values():
        MapID = Models.EditLevel.fetch_LastMapID() +1 
        fileName = "../ICT2101/Levels/"+str(MapID)+".txt"
        dbfilePath = "Levels/"+str(MapID)+".txt"
        fileObj = open(fileName,"w+")
        processCommands(fileObj, CommandList) 
        dbStatus = Models.EditLevel.insert_Level(Difficulty, LevelName, dbfilePath)
        processGrid(fileObj, MapDict)
        fileObj.close()  
        return 'success'
    else:
        return 'fail'


    


        
'''
Process Commands 
    Check the commands provide by user in the list and insert to file 
    Commands Order:
        1) Move Upward 
        2) Move Downward 
        3) Move Left
        4) Move Right
        5) Repeat 
    If command is present it is indicated with 1 in the text file in the order stated above. 
    The 1st line in the text file is used to indicate commands provided.
        @param CommandList The id list of checked commands
        @param fileObj file object
'''   

def processCommands(fileObj, CommandList):
    for i in range(1,6):
        if str(i) in CommandList:
            if i == 5:
                fileObj.write('1' +'\n')
            else:
                fileObj.write('1')
        else:
            if i == 5:
                fileObj.write('0' +'\n')
            else:
                fileObj.write('0')

'''
Process Grid
    Check the sprites provide by user for each grid and insert to file.
    The 5x5 grid is inserted as values stated below. 
    Find Grid Type is used to get repective value of sprite.
        @param MapDict (Position: Sprite) key and value pair 
        @param fileObj file object
''' 
def processGrid(fileObj, MapDict):
    fileObj.write('1')
    for i in range(2,26):
        if str(i) in MapDict.keys():
            writevalue = findGridType(MapDict.get(str(i)))
            if i%5 == 0:
                fileObj.write(writevalue +'\n')
            else: 
                fileObj.write(writevalue)
        else:
            if i%5 == 0:
                fileObj.write('0' +'\n')
            else: 
                fileObj.write('0')

'''
Find Grid Type
    Values:
        0 = empty
        1 = car
        2 = wall
        3 = coin
        4 = goal
    Each value represent on one box on grid map
        @param gridType Sprite value
''' 
def findGridType(gridType):
    if (gridType == 'wall'):
        return '2'
    elif (gridType == 'coins'):
        return '3'
    elif (gridType == 'goal'):
        return '4'

