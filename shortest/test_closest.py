from shortest.closest import closest
import unittest

class TestClosest(unittest.TestCase):
    def test_closest(self):
        p1 = [3,4]
        p2 = [5,6]

        p1_ans, p2_ans,close = closest([[3,4],[5,6]])
        self.assertEqual(p1,p1_ans)
        self.assertEqual(p2,p2_ans)
        self.assertEqual(close,2)

    def test_closest_in_list(self):
        p1 = [2,2]
        p2 = [3,3]
        p3 = [4,6]
        d = 1
        p1_ans, p2_ans, close = closest([p1,p2,p3])
        self.assertEqual(p1_ans,p1)
        self.assertEqual(p2_ans, p2)
        self.assertEqual(close, d)
        
if __name__ == '__main__':
    unittest.main()
