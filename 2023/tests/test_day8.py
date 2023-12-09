import unittest

from day8 import main

test_data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test_data2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

class TestDay8(unittest.TestCase):
    
    def test_main(self):
        # self.assertEqual(main(test_data), 2)
        self.assertEqual(main(test_data2), 6)
