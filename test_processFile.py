# Python Test lib 
import unittest
import Models.processFile




class TestProcessFile(unittest.TestCase):
    
    def test_processCommands(self):
        fileName = "testfile.txt"
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



