# Python Test lib 
import unittest
import Models.processFile


class TestProcessFile(unittest.TestCase):
    """
    Whitebox testing code for processFile
    """
    def test_processCommands(self):
        fileName = "test_processCommandsfile.txt"
        fileObj = open(fileName,"w+")

        # Assertion 1: covers line 1-2,3,4-5,16
        CommandList = ['1','2','3','4','5','5']
        fileObj.write('Assertion 1:' +'\n')
        result = Models.processFile.processCommands(fileObj, CommandList)
        self.assertEqual(result, 'not written')

        # Assertion 2: covers line 1-2,3,4-5,16
        CommandList = ['7']
        fileObj.write('Assertion 2:' +'\n')
        result = Models.processFile.processCommands(fileObj, CommandList)
        self.assertEqual(result, 'not written')

        # Assertion 3: covers line 1-2,3,11-12,13,14,16
        CommandList = []
        fileObj.write('Assertion 3:' +'\n')
        result = Models.processFile.processCommands(fileObj, CommandList)
        self.assertEqual(result, 'written 0')

        # Assertion 4: covers line 1-2,3,7-8,9,10
        CommandList = ['1','2','3','4', '5']
        fileObj.write('Assertion 4:' +'\n')
        result = Models.processFile.processCommands(fileObj, CommandList)
        self.assertEqual(result, 'written 1')
        fileObj.close()  

    def test_findGridType(self):
        # Assertion 1: 1,2,7
        result = Models.processFile.findGridType("wall")
        self.assertEqual(result, "2")

        # Assertion 2: 1,4,7
        result = Models.processFile.findGridType("coins")
        self.assertEqual(result, "3")

        # Assertion 2: 1,5,7
        result = Models.processFile.findGridType("goal")
        self.assertEqual(result, "4")

        # Assertion 2: 1,6,7
        result = Models.processFile.findGridType("test")
        self.assertEqual(result, "no match")

    def test_processGrid(self):
        fileName = "test_processGridfile.txt"
        fileObj = open(fileName,"w+")
        # Assertion 1
        MapDict = {'9': 'goal', '10': 'wall', '25': 'chicken'}
        fileObj.write('Assertion 1:' +'\n')
        result = Models.processFile.processGrid(fileObj,MapDict)
        self.assertEqual(result, "sprite out of range")

        # Assertion 2
        MapDict = {'9': 'goal', '10': 'wall', '25': 'coins'}
        fileObj.write('Assertion 1:' +'\n')
        result = Models.processFile.processGrid(fileObj,MapDict)
        self.assertEqual(result, "got sprite")

        # Assertion 3
        MapDict = {}
        fileObj.write('Assertion 1:' +'\n')
        result = Models.processFile.processGrid(fileObj,MapDict)
        self.assertEqual(result, "no sprite")
        fileObj.close()  

    def test_writeToMapFile(self):
        # Assertion 1
        Maparray = [{'position': '2', 'type': 'coins'}, {'position': '20', 'type': 'wall'}, {'position': '24', 'type': 'coins'}, {'position': '3', 'type': 'coins'}]
        LevelName = 'May_Game'
        CommandList = ['1', '2', '3', '4']
        Difficulty = 2
        result = Models.processFile.writeToMapFile(Maparray,LevelName,CommandList, Difficulty)
        self.assertEqual(result, "not inserted")

        # Assertion 2
        Maparray = [{'position': '2', 'type': 'coins'}, {'position': '20', 'type': 'wall'}, {'position': '24', 'type': 'goal'}, {'position': '3', 'type': 'coins'}]
        LevelName = 'May_Game'
        CommandList = ['1', '2', '3', '4']
        Difficulty = 2
        result = Models.processFile.writeToMapFile(Maparray,LevelName,CommandList, Difficulty)
        self.assertEqual(result, "success")

        # Assertion 3
        Maparray = [{'position': '2', 'type': 'coins'}, {'position': '20', 'type': 'wall'}, {'position': '24', 'type': 'goal'}, {'position': '3', 'type': 'coins'}]
        LevelName = 'May_Game'
        CommandList = ['7']
        Difficulty = 2
        result = Models.processFile.writeToMapFile(Maparray,LevelName,CommandList, Difficulty)
        self.assertEqual(result, "Command Error")

        # Assertion 4
        Maparray = [{'position': '2', 'type': 'coins'}, {'position': '20', 'type': 'ball'}, {'position': '24', 'type': 'goal'}, {'position': '3', 'type': 'coins'}]
        LevelName = 'May_Game'
        CommandList = ['1', '2', '3', '4']
        Difficulty = 2
        result = Models.processFile.writeToMapFile(Maparray,LevelName,CommandList, Difficulty)
        self.assertEqual(result, "Sprite Error")

if __name__ == '__main__':
    unittest.main()