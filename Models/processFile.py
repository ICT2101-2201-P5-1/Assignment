import Models.EditLevel


'''
Edit Level
    Handle receiving of POST request from Map and rendering of CreateLevel page 
        @param jsdata The data transfered from drag & drop interface 
        @param JSON_obj JSON object in position: "2", value:"goal"
        @param mapList global array 
        @return the CreateLevel.html page 
'''
def writeToMapFile(Maparray,LevelName,CommandList, Difficulty):
    MapDict ={}
    for grid in Maparray:
        MapDict[grid['position']]= grid['type']
    if 'goal' in MapDict.values():
        fileName = "../ICT2101/Levels/"+LevelName+".txt"
        dbfilePath = "/Levels/"+LevelName+".txt"
        fileObj = open(fileName,"w+")
        processCommands(fileObj, CommandList) 
        dbStatus = Models.EditLevel.insert_Level(Difficulty, LevelName, dbfilePath)
        processGrid(fileObj, MapDict)
        fileObj.close()  
        return 'success'
    else:
        return 'fail'


    


        
     


def processCommands(fileObj, CommandList):
    for i in range(1,8):
        if str(i) in CommandList:
            if i == 7:
                fileObj.write('1' +'\n')
            else:
                fileObj.write('1')
        else:
            if i == 7:
                fileObj.write('0' +'\n')
            else:
                fileObj.write('0')


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


def findGridType(gridType):
    if (gridType == 'wall'):
        return '2'
    elif (gridType == 'coins'):
        return '3'
    elif (gridType == 'goal'):
        return '4'

