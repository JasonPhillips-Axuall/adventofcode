
import unittest

from day5 import build_map, build_map_names, combine_maps, main, non_overlapping_span

test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

class TestDay5(unittest.TestCase):

    # def test_build_names(self):
    #     self.assertEqual(build_map_names("seed-to-soil map:"), 'seed-to-soil')
    #     self.assertEqual(build_map_names("soil-to-fertilizer map:"), 'soil-to-fertilizer')
        
    def test_non_overlapping_span(self):
        n = non_overlapping_span([0, 5, 1], [4, 10, 1])
        self.assertEqual(len(n), 3)
        self.assertEqual(n[0][0], 0)
        self.assertEqual(n[0][1], 3)

        self.assertEqual(n[1][0], 4)
        self.assertEqual(n[1][1], 5)

        self.assertEqual(n[2][0], 6)
        self.assertEqual(n[2][1], 10)

        n = non_overlapping_span([50, 97, 2], [52, 53, -15])
        self.assertEqual(len(n), 3)

        self.assertEqual(n[0][0], 50)
        self.assertEqual(n[0][1], 51)

        self.assertEqual(n[1][0], 52)
        self.assertEqual(n[1][1], 53)

        self.assertEqual(n[2][0], 54)
        self.assertEqual(n[2][1], 97)

    def test_combine_maps(self):
        pass
        # maps = [[[0, 14, 39], [15, 51, -15], [50, 97, 2], [52, 53, -15], [98, 99, -48]]]
        # ans = [[[0, 14, 39], [15, 49, -15], [50, 51, 2], [52, 53, -15], [98, 99, -48]]]
        # combined = combine_maps(maps)
        # self.assertEqual(combined, ans)


    def test_main(self):
        pass
        # self.assertEqual(main(test_data), 35)
        # self.assertEqual(main(test_data), 46)
