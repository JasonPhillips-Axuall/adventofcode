import unittest

from day2 import count_cubes, cube_parts, get_game_number, is_line_valid, is_valid_game, exec, count_minimun_cubes, get_cube_minimum, get_cube_power


class TestDay2(unittest.TestCase):
    def test_cube_parts(self):
        test_data = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        ans = cube_parts(test_data)
        self.assertEqual(ans, ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"])

    def test_count_cubes(self):
        self.assertEqual(count_cubes("3 blue, 4 red"), {"red": 4, "blue": 3, "green": 0})
        self.assertEqual(count_cubes("1 red, 2 green, 6 blue"), {"red": 1, "blue": 6, "green": 2})
        self.assertEqual(count_cubes("1 red, 2 red, 6 blue"), {"red": 3, "blue": 6, "green": 0})

    def test_valid(self):
        self.assertTrue(is_valid_game({"red": 12, "green": 13, "blue": 14}))
        self.assertFalse(is_valid_game({"red": 12, "green": 13, "blue": 15}))

    def test_is_line_valid(self):
        self.assertTrue(is_line_valid("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
        self.assertTrue(is_line_valid("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"))
        self.assertTrue(is_line_valid("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"))

        self.assertFalse(is_line_valid("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"))
        self.assertFalse(is_line_valid("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"))

    def test_get_game_from_line(self):
        self.assertEqual(get_game_number("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), "1")
        self.assertEqual(get_game_number("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"), "2")
        self.assertEqual(get_game_number("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"), "5")

    def test_count_minimun_cubes(self):
        self.assertEqual(count_minimun_cubes("3 blue, 4 blue", {"red": 0, "green": 0, "blue": 0}), {"red": 0, "blue": 4, "green": 0})
    
    def test_count_minimum_per_line(self):
        self.assertEqual(get_cube_minimum("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), {"red": 4, "blue": 6, "green": 2})
        self.assertEqual(get_cube_minimum("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"), {"red": 1, "blue": 4, "green": 3})
        self.assertEqual(get_cube_minimum("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"), {"red": 20, "blue": 6, "green": 13})
        self.assertEqual(get_cube_minimum("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"), {"red": 14, "blue": 15, "green": 3})
        self.assertEqual(get_cube_minimum("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"), {"red": 6, "blue": 2, "green": 3})

    def test_powers(self):
        self.assertEqual(get_cube_power(get_cube_minimum("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")), 48)
        self.assertEqual(get_cube_power(get_cube_minimum("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")), 12)
        self.assertEqual(get_cube_power(get_cube_minimum("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")), 1560)
        self.assertEqual(get_cube_power(get_cube_minimum("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")), 630)
        self.assertEqual(get_cube_power(get_cube_minimum("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")), 36)

        
    def test_part1(self):
        test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

        # self.assertEqual(exec(test_data), 8)
        self.assertEqual(exec(test_data), 2286)
