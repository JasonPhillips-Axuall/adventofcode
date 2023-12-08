import unittest

from day7 import calc_hand, hand_value, is_five_of_a_kind, is_four_of_a_kind, is_3_of_a_kind, is_full_house, is_2_of_a_kind, is_two_pair, main

class TestDay7(unittest.TestCase):

    def test_of_a_kind(self):
        
        self.assertTrue(is_five_of_a_kind(['2', '2', '2', '2', '2']))
        self.assertTrue(is_five_of_a_kind(['A', 'A', 'A', 'A', 'A']))

        self.assertTrue(is_four_of_a_kind(['2', '2', '2', '2', '1']))
        self.assertTrue(is_four_of_a_kind(['2', '2', '2', '2', '3']))
        self.assertTrue(is_four_of_a_kind(['A', 'A', 'A', 'A', 'B']))

        self.assertFalse(is_3_of_a_kind(['2', '2', '2', '1', '1']))

        self.assertTrue(is_3_of_a_kind(['2', '2', '2', '1', '3']))
        self.assertTrue(is_3_of_a_kind(['2', '2', '2', '4', '3']))
        self.assertTrue(is_3_of_a_kind(['A', 'A', 'A', '1', 'B']))

        self.assertTrue(is_3_of_a_kind(['2', '2', '2', '1', '3']))
        self.assertTrue(is_3_of_a_kind(['2', '2', '2', '4', '3']))
        self.assertTrue(is_3_of_a_kind(['A', 'A', 'A', '1', 'B']))

    def test_two_of_a_kind(self):
        self.assertFalse(is_2_of_a_kind(['2', '2', '5', '1', '1']))
        self.assertTrue(is_2_of_a_kind(['2', '2', '5', '1', '3']))
        self.assertTrue(is_2_of_a_kind(['2', '2', '5', '4', '3']))
        self.assertTrue(is_2_of_a_kind(['A', 'A', '5', '1', 'B']))

    def test_two_pair(self):
        self.assertTrue(is_two_pair(['2', '2', '5', '1', '1']))
        self.assertTrue(is_two_pair(['2', '2', '1', '1', '3']))
        self.assertTrue(is_two_pair(['2', '2', '5', '4', '4']))
        self.assertTrue(is_two_pair(['A', 'A', '5', 'K', 'K']))

    def test_is_full_house(self):
        self.assertTrue(is_full_house(['A', 'A', '1', '1', '1']))
        self.assertFalse(is_full_house(['A', 'A', 'K', '1', '1']))
        self.assertFalse(is_full_house(['A', 'K', '1', '1', '1']))


    def test_hand_value(self):
        self.assertEqual(hand_value(['1', '1', '1', '1', '1']), '0101010101')
        self.assertEqual(hand_value(['2', '2', '2', '2', '2']), '0202020202')
        self.assertEqual(hand_value(['T','T']), '1010')
        self.assertEqual(hand_value(['K','T','J','J','T']), '1310111110')


    def test_main(self):
        test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
        assert(main(test_data), 6440)