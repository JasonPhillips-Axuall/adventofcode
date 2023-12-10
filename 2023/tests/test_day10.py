import unittest

from day10 import main, next

test_data = """.....
.S-7.
.|.|.
.L-J.
....."""

test_data2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

class TestDay10(unittest.TestCase):

    def test_main(self):
        # self.assertEqual(main(test_data), 4)
        self.assertEqual(main(test_data2), 8)