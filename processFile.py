def writeToMapFile(Maparray,LevelName,CommandList, Difficulty):
    fileObj = open("../ICT2101/Levels/"+LevelName+".txt","w+")
    print(Maparray,LevelName,CommandList, Difficulty)
    processCommands(fileObj, CommandList)
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
