def writeToMapFile(Maparray,LevelName,CommandList, Difficulty):
    fileObj = open("../ICT2101/Levels/"+LevelName+".txt","w+")
    print(Maparray,LevelName,CommandList, Difficulty)
    processCommands(fileObj, CommandList)
    MapDict ={}
    for grid in Maparray:
        MapDict[grid['position']]= grid['type']
    processGrid(fileObj, MapDict)
    fileObj.close()   


def processCommands(fileObj, CommandList):
    if('C1' in CommandList):
        fileObj.write('1')
    else:
        fileObj.write('0')

    if('C2' in CommandList):
        fileObj.write('1')
    else:
        fileObj.write('0')

    if('C3' in CommandList):
        fileObj.write('1')
    else:
        fileObj.write('0')

    if('C4' in CommandList):
        fileObj.write('1')
    else:
        fileObj.write('0')

    if('C5' in CommandList):
        fileObj.write('1')
    else:
        fileObj.write('0')

    if('C6' in CommandList):
        fileObj.write('1')
    else:
        fileObj.write('0')

    if('C7' in CommandList):
        fileObj.write('1\n')
    else:
        fileObj.write('0\n')


def processGrid(fileObj, MapDict):
    fileObj.write('1')
    if('2' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('2'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('3' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('3'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('4' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('4'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('5' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('5'))
        fileObj.write(writevalue +'\n')
    else:
        fileObj.write('0\n')

    if('6' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('6'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')


    if('7' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('7'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('8' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('8'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('9' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('9'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('10' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('10'))
        fileObj.write(writevalue +'\n')
    else:
        fileObj.write('0\n')

    if('11' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('11'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')


    if('12' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('12'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('13' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('13'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('14' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('14'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('15' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('15'))
        fileObj.write(writevalue +'\n')
    else:
        fileObj.write('0\n')

    if('16' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('16'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('17' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('17'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('18' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('18'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('19' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('19'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('20' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('20'))
        fileObj.write(writevalue +'\n')
    else:
        fileObj.write('0\n')

    if('21' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('21'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('22' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('22'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('23' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('23'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('24' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('24'))
        fileObj.write(writevalue)
    else:
        fileObj.write('0')

    if('25' in MapDict.keys()):
        writevalue = findGridType(MapDict.get('25'))
        fileObj.write(writevalue +'\n')
    else:
        fileObj.write('0\n')    

    
    
def findGridType(gridType):
    if (gridType == 'wall'):
        return '2'
    elif (gridType == 'coins'):
        return '3'
    elif (gridType == 'goal'):
        return '4'

