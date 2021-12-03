from Models.editLevel import init_connection_sql, fetchPassword, insert_Level, fetch_LastMapID
import unittest


class TestEditLevel(unittest.TestCase):
    """
    Whitebox testing code for edit level.
    """
    def test_init_connection_sql(self):
        result = init_connection_sql()
        self.assertIsNotNone(result)
    
    def test_fetchPassword(self):
        pw = []
        result = fetchPassword()
        for i in result:
            pw.append(i[0])
            res = i[0]
        self.assertEqual(res, 'admin')
        
    # This will insert something into the DB
    def test_insert_Level(self):
        result = insert_Level(2, "testMap5", 'Levels/555.txt')
        print(result)
        self.assertEqual(result, "Insert Level success")
    
    def test_fetch_LastMapID(self):
        result = fetch_LastMapID()
        # Ensure that the 2nd argument in below is same as the latest map_id
        self.assertIs(result, 34)


if __name__ == '__main__':
    unittest.main()