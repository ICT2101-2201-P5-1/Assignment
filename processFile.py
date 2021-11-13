def writeToMapFile(Maparray,LevelName,CommandList, Difficulty):
    f= open("../ICT2101/Levels/map1.txt","w+")
    print(Maparray,LevelName,CommandList, Difficulty)
    for item in Maparray:
        if(item['position']=='3-4'):
            f.write("added to positiom\r\n")
    f.close()