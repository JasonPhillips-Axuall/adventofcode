import unittest

from day11 import get_all_adistance, get_expands, get_galaxy_list, main, make_grid

test_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

class TestDay11(unittest.TestCase):

    def test_exp(self):

        self.assertEqual(main(test_data, 1), 292)
        self.assertEqual(main(test_data, 2), 374)
        self.assertEqual(main(test_data, 10), 1030)
        self.assertEqual(main(test_data, 100), 8410)

        # self.assertEqual(main(test_data, 1000000), 513171773355)

    # def test_main(self):
    #     self.assertEqual(main(test_data), 374)

    