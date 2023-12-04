import unittest

from day3 import token_indexes, has_symbol_between, main, get_gear_list

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
        self.assertEqual(token_indexes("467..114.."), [(0, 3, '467'), (5, 8, '114')])
        
        self.assertEqual(len(token_indexes("...*......")), 0)
        self.assertEqual(len(token_indexes("..35..633.")), 2)
        self.assertEqual(token_indexes("..35..633."), [(2, 4, '35'), (6, 9, '633')])

    def test_get_gear_list(self):
        self.assertEqual(get_gear_list((0, 2, '*'), [], [(0, 3, '467')]), [467])
        self.assertEqual(get_gear_list((0, 2, '*'), [], [(1, 5, '467')]), [467])
        self.assertEqual(get_gear_list((0, 2, '*'), [], [(3, 5, '467')]), [])

        self.assertEqual(get_gear_list((2, 3, '*'), [], [(1, 5, '467'), (3, 4, '122')]), [467, 122])
        
    def test_has_adjacent_symbol(self):
        self.assertTrue(has_symbol_between("...*......", 1, 3, symbol_regex))
        
        self.assertFalse(has_symbol_between("617*......", 7,9, symbol_regex))
        self.assertFalse(has_symbol_between(".....+.58.", 7,9, symbol_regex))
        self.assertFalse(has_symbol_between("..592.....", 7,9, symbol_regex))
        
        self.assertEqual(main("......755.\n...$.*....\n.664.598.."), 451490)
        self.assertEqual(main("2*2"), 4)

        self.assertEqual(main(test_data), 467835)