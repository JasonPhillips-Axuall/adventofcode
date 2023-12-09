import unittest

from day9 import build_seq, build_step, main


class TestDay9(unittest.TestCase):
    # def test_step(self):
    #     seq = [0, 3, 6, 9, 12, 15]
    #     self.assertEqual(build_step(seq), [3, 3, 3, 3, 3])

    # def test_build_seq(self):
    #     seq = '0 3 6 9 12 15'
    #     ans = [[0, 3, 6, 9, 12, 15, 18], [3, 3, 3, 3, 3, 3], [0, 0, 0, 0, 0]]
    #     self.assertEqual(build_seq(seq), ans)
    #     seq = '1   3   6  10  15  21'
    #     ans = [[1, 3, 6, 10, 15, 21, 28], [2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1], [0, 0, 0, 0]]
    #     self.assertEqual(build_seq(seq), ans)

    #     seq = '10  13  16  21  30  45'
    #     ans = [[10, 13, 16, 21, 30, 45, 68], [3, 3, 5, 9, 15, 23], [0, 2, 4, 6, 8], [2, 2, 2, 2], [0, 0, 0]]
    #     self.assertEqual(build_seq(seq), ans)

    def test_main(self):
        # self.assertEqual(main('0 3 6 9 12 15'), 18)
#         self.assertEqual(main('1   3   6  10  15  21'), 28)
        self.assertEqual(main('10  13  16  21  30  45'), 5)
#         self.assertEqual(main("""0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""), 114)