import os
import unittest
from day1 import exec, get_first_number, get_last_number, get_number_str

here = os.path.dirname(os.path.abspath(__file__))

test_data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

class TestDay1(unittest.TestCase):

    def test_get_first_number(self):
        self.assertEqual(get_first_number("two1nine"), "2")
        self.assertEqual(get_first_number("eightwothree"), "8")
        self.assertEqual(get_first_number("abcone2threexyz"), "1")
        self.assertEqual(get_first_number("xtwone3four"), "2")
        self.assertEqual(get_first_number("4nineeightseven2"), "4")
        self.assertEqual(get_first_number("zoneight234"), "1")
        self.assertEqual(get_first_number("7pqrstsixteen"), "7")

    def test_get_last_number(self):
        self.assertEqual(get_last_number("two1nine"), "9")
        self.assertEqual(get_last_number("eightwothree"), "3")
        self.assertEqual(get_last_number("abcone2threexyz"), "3")
        self.assertEqual(get_last_number("xtwone3four"), "4")
        self.assertEqual(get_last_number("4nineeightseven2"), "2")
        self.assertEqual(get_last_number("zoneight234"), "4")
        self.assertEqual(get_last_number("7pqrstsixteen"), "6")

    def test_first_last(self):
        self.assertEqual(get_first_number("1"), "1")
        self.assertEqual(get_last_number("1"), "1")
        test_data = "81s"
        self.assertEqual(get_number_str(test_data), "81")

    def test_part2(self):
        ans = exec(test_data)
        self.assertEqual(ans, 281)

        with open(os.path.join(here, "../../data/2023/1.txt"), "r") as data:
            ans = exec(data.read())
            self.assertEqual(ans, 55902)