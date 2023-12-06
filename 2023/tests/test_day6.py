import unittest

from day6 import calc_run_distance, calc_valid_run, main

test_data="""Time:      7  15   30\nDistance:  9  40  200"""

class TestDay6(unittest.TestCase):

    def test_calc_run_distance(self):
        self.assertEqual(calc_run_distance(7, 0), 0)
        self.assertEqual(calc_run_distance(7, 1), 6)
        self.assertEqual(calc_run_distance(7, 2), 10)
        self.assertEqual(calc_run_distance(7, 3), 12)
        self.assertEqual(calc_run_distance(7, 4), 12)
        self.assertEqual(calc_run_distance(7, 5), 10)
        self.assertEqual(calc_run_distance(7, 6), 6)
        self.assertEqual(calc_run_distance(7, 7), 0)

    def test_calc_valid_run(self):
        self.assertEqual(len(calc_valid_run(7, 9)), 4)
        self.assertEqual(len(calc_valid_run(15, 40)), 8)
        self.assertEqual(len(calc_valid_run(30, 200)), 9)


    def test_main(self):
        # self.assertEqual(main(test_data), 288)
        self.assertEqual(main(test_data), 71503)
