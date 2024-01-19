import number_of_ways as nw 
import number_of_ways_recursion as nwr 
import unittest

class Test_TestNumberOfWays(unittest.TestCase):
    def test_number_of_ways(self):
        self.assertEqual(nw.number_of_ways(1, 2, 3), 3)

    def test_number_of_ways_recursion(self):
        self.assertEqual(nw.number_of_ways(1, 2, 3), 3)


if __name__ == '__main__':
    unittest.main()