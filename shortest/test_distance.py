from shortest.distance import distance
from shortest.distance import distance
import unittest

class TestDistance(unittest.TestCase):
    def test_normal_points(self):
        first = [3,4]
        second = [5,6]
        expected = 2
        ans = distance(first,second)
        self.assertEqual(expected,ans,msg="the distance between the provided points is not equal")
    
    def test_distance_is_zero(self):
        first = [3,4]
        ans = distance(first, first)
        self.assertEqual(0,ans, msg="distance between the two points should be 0")

if __name__ == '__main__':
    unittest.main()