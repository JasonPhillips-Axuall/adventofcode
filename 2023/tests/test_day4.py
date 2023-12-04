import unittest

from day4 import calc_winning_points, get_winning, get_player, wining_count, main

test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

class TestDay4(unittest.TestCase):
    def test_winning_number_set(self):
        self.assertAlmostEqual(get_winning('41 48 83 86 17 | 83 86  6 31 17  9 48 53'), set([83, 86, 6, 31, 17, 9, 48, 53]))
        self.assertAlmostEqual(get_player('41 48 83 86 17 | 83 86  6 31 17  9 48 53'), set([41, 48, 83, 86, 17 ]))

    def test_count_winning_set(self):
        self.assertEqual(wining_count(set([1,2,3]), set([1,2,3])), 3)
        self.assertEqual(wining_count(set([1,2,3]), set([1,2])), 2)

        self.assertEqual(wining_count(set([83, 86, 6, 31, 17, 9, 48, 53]), set([41, 48, 83, 86, 17 ])), 4)

    def test_score(self):
        self.assertEqual(calc_winning_points(0), 0)
        self.assertEqual(calc_winning_points(1), 1)
        self.assertEqual(calc_winning_points(2), 2)
        self.assertEqual(calc_winning_points(3), 4)
        self.assertEqual(calc_winning_points(4), 8)
    
    def test_main(self):
        self.assertEqual(main("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")[0], 8)
        self.assertEqual(main("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")[0], 2)
        self.assertEqual(main("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")[0], 2)
        self.assertEqual(main("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83")[0], 1)
        self.assertEqual(main("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")[0], 0)
        self.assertEqual(main("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")[0], 0)

        self.assertEqual(main(test_data)[0], 13)
