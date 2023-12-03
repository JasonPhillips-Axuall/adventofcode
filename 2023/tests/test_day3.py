import unittest

from day3 import token_indexes, has_symbol_between, exec

test_data="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

number_regex = r"\d+"
symbol_regex = r"[^A-Za-z0-9.]"
gear_regex = r"[*]"

class TestDay2(unittest.TestCase):
    def test_has_token(self):
        
        self.assertEqual(len(token_indexes("467..114..")), 2)
        self.assertEqual(token_indexes("467..114.."), [(0, 3), (5, 8)])
        
        self.assertEqual(len(token_indexes("...*......")), 0)
        self.assertEqual(len(token_indexes("..35..633.")), 2)
        self.assertEqual(token_indexes("..35..633."), [(2, 4), (6, 9)])


    def test_has_adjacent_symbol(self):
        # self.assertTrue(has_symbol_between("...*......", 1, 3, symbol_regex))
        
        # self.assertFalse(has_symbol_between("617*......", 7,9, symbol_regex))
        # self.assertFalse(has_symbol_between(".....+.58.", 7,9, symbol_regex))
        # self.assertFalse(has_symbol_between("..592.....", 7,9, symbol_regex))

        # self.assertEqual(exec("467..114..\n...*......"), 467)
        # self.assertEqual(exec("...*......\n..35..633."), 35)
        # self.assertEqual(exec("......755.\n...$.*...."), 755)
        # self.assertEqual(exec("467..114..\n...*......\n..35..633."), 16345)
        
        # self.assertEqual(exec("......755.\n...$.*....\n.664.598.."), 451490)
        self.assertEqual(exec(test_data), 467835)
        self.assertEqual(exec(""".........677..
.%..863..#....
46...*.....475
......470.*...
..........587."""), (863*470)+(475*587))
        
        self.assertEqual(exec("""..730..35..
......*....
......453.."""), 35*453)
        
        self.assertEqual(exec("""863..#
.*....
..470."""), 863*470)
