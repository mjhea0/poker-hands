import os
import unittest

from poker import get_rounds, check_royal_flush, create_readable_cards, \
    get_score, check_straight_flush, check_four_of_a_kind, \
    check_three_of_a_kind, check_if_same_suit, check_straight, \
    check_two_pairs, check_full_house, check_one_pair, play


class TestPoker(unittest.TestCase):

    def test_get_rounds(self):
        filename = os.path.join('files', 'p054_poker.txt')
        rounds = get_rounds(filename)
        self.assertEqual(len(rounds), 1000)

    def test_check_royal_flush(self):
        hand1 = 'TC JC QC KC AC'
        hand2 = 'TD JS QD KS AC'
        hand3 = 'TC JC QC KC 9C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        self.assertTrue(check_royal_flush(cards1))
        self.assertFalse(check_royal_flush(cards2))
        self.assertFalse(check_royal_flush(cards3))

    def test_check_straight_flush(self):
        hand1 = '2C 3C 4C 5C 6C'
        hand2 = '2D 3S 4D 5S 6C'
        hand3 = '2C 8C 4C 5C 6C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        self.assertTrue(check_straight_flush(cards1))
        self.assertFalse(check_straight_flush(cards2))
        self.assertFalse(check_straight_flush(cards3))

    def test_check_four_of_a_kind(self):
        hand1 = '2C 2C 2C 2C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = '3S 2C 3C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        self.assertTrue(check_four_of_a_kind(cards1))
        self.assertTrue(check_four_of_a_kind(cards2))
        self.assertFalse(check_four_of_a_kind(cards3))
        self.assertTrue(check_four_of_a_kind(cards4))

    def test_check_full_house(self):
        hand1 = '2C 2C 2C 6C 6C'
        hand2 = '2D 3S 3D 2S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = '3S 2C 3C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        self.assertTrue(check_full_house(cards1))
        self.assertTrue(check_full_house(cards2))
        self.assertFalse(check_full_house(cards3))
        self.assertFalse(check_full_house(cards4))

    def test_check_flush(self):
        hand1 = '2C 2C 2C 2C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = '3S 2C 3C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        self.assertTrue(check_if_same_suit(cards1['suits']))
        self.assertFalse(check_if_same_suit(cards2['suits']))
        self.assertTrue(check_if_same_suit(cards3['suits']))
        self.assertFalse(check_if_same_suit(cards4['suits']))

    def test_check_straight(self):
        hand1 = '2C 2C 2C 2C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = 'TS JS QC KC AC'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        self.assertFalse(check_straight(cards1))
        self.assertFalse(check_straight(cards2))
        self.assertFalse(check_straight(cards3))
        self.assertTrue(check_straight(cards4))

    def test_check_three_of_a_kind(self):
        hand1 = '2C 2C 2C 2C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = '3S 2C 3C 3C 3C'
        hand5 = '3S 2C 6C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        cards5 = create_readable_cards(hand5.split(' '))
        self.assertTrue(check_three_of_a_kind(cards1))
        self.assertTrue(check_three_of_a_kind(cards2))
        self.assertFalse(check_three_of_a_kind(cards3))
        self.assertTrue(check_three_of_a_kind(cards4))
        self.assertTrue(check_three_of_a_kind(cards5))

    def test_check_two_pairs(self):
        hand1 = '2C 2C 3C 3C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = '3S 2C 3C 3C 2C'
        hand5 = '3S 2C 6C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        cards5 = create_readable_cards(hand5.split(' '))
        self.assertTrue(check_two_pairs(cards1))
        self.assertFalse(check_two_pairs(cards2))
        self.assertFalse(check_two_pairs(cards3))
        self.assertTrue(check_two_pairs(cards4))
        self.assertFalse(check_two_pairs(cards5))

    def test_check_one_pair(self):
        hand1 = '2C 2C 3C 4C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = '3S 2C 3C 3C 2C'
        hand5 = '3S 2C 6C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        cards5 = create_readable_cards(hand5.split(' '))
        self.assertTrue(check_one_pair(cards1))
        self.assertTrue(check_one_pair(cards2))
        self.assertFalse(check_one_pair(cards3))
        self.assertFalse(check_one_pair(cards4))
        self.assertTrue(check_one_pair(cards5))

    def test_get_score_royal_flush(self):
        hand1 = 'TC JC QC KC AC'
        hand2 = 'TD JS QD KS AC'
        hand3 = 'TC JC QC KC 9C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        self.assertEqual(get_score(cards1), 10)
        self.assertNotEqual(get_score(cards2), 10)
        self.assertNotEqual(get_score(cards3), 10)

    def test_get_score_straight_flush(self):
        hand1 = 'TC JC QC KC AC'
        hand2 = 'TD JS QD KS AC'
        hand3 = 'TC JC QC KC 9C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        self.assertNotEqual(get_score(cards1), 9)
        self.assertNotEqual(get_score(cards2), 9)
        self.assertEqual(get_score(cards3), 9)

    def test_get_score_four_of_a_kind(self):
        hand1 = '2C 2C 2C 2C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = '3S 2C 3C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        self.assertEqual(get_score(cards1), 8)
        self.assertEqual(get_score(cards2), 8)
        self.assertNotEqual(get_score(cards3), 8)
        self.assertEqual(get_score(cards4), 8)

    def test_get_score_full_house(self):
        hand1 = '2C 6S 2C 2C 6C'
        hand2 = '2D 3S 2D 3S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = '3S 2C 3C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        self.assertEqual(get_score(cards1), 7)
        self.assertEqual(get_score(cards2), 7)
        self.assertNotEqual(get_score(cards3), 7)
        self.assertNotEqual(get_score(cards4), 7)

    def test_get_score_flush(self):
        hand1 = '2C 2C 2C 2C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = '3S 2C 3C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        self.assertNotEqual(get_score(cards1), 6)
        self.assertNotEqual(get_score(cards2), 6)
        self.assertEqual(get_score(cards3), 6)
        self.assertNotEqual(get_score(cards4), 6)

    def test_get_score_straight(self):
        hand1 = '2C 2C 2C 2C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '3C 7C 4S 5C 6C'
        hand4 = 'TS JS QC KC AC'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        self.assertNotEqual(get_score(cards1), 5)
        self.assertNotEqual(get_score(cards2), 5)
        self.assertEqual(get_score(cards3), 5)
        self.assertEqual(get_score(cards4), 5)

    def test_get_score_three_of_a_kind(self):
        hand1 = '2C 2C 2C 2C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '2C 8C 4C 5C 6C'
        hand4 = '3S 2C 3C 3C 3C'
        hand5 = '3S 2C 6C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        cards5 = create_readable_cards(hand5.split(' '))
        self.assertNotEqual(get_score(cards1), 4)
        self.assertNotEqual(get_score(cards2), 4)
        self.assertNotEqual(get_score(cards3), 4)
        self.assertNotEqual(get_score(cards4), 4)
        self.assertEqual(get_score(cards5), 4)

    def test_get_score_two_pairs(self):
        hand1 = '2C 2C 3C 3C 6S'
        hand2 = '2D 3S 4D 2S 2C'
        hand3 = '2C 2C 4S 5C 5C'
        hand4 = '3S 2C 3C 3C 2C'
        hand5 = '3S 2C 6C 3C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        cards5 = create_readable_cards(hand5.split(' '))
        self.assertEqual(get_score(cards1), 3)
        self.assertNotEqual(get_score(cards2), 3)
        self.assertEqual(get_score(cards3), 3)
        self.assertNotEqual(get_score(cards4), 3)
        self.assertNotEqual(get_score(cards5), 3)

    def test_get_score_one_pair(self):
        hand1 = '2C 2C 3S 4C 6C'
        hand2 = '2D 3S 2D 2S 2C'
        hand3 = '2C 8S 4C 8C 6C'
        hand4 = '3S 2C 3C 3C 2C'
        hand5 = '3S 2C 6C 7C 3C'
        cards1 = create_readable_cards(hand1.split(' '))
        cards2 = create_readable_cards(hand2.split(' '))
        cards3 = create_readable_cards(hand3.split(' '))
        cards4 = create_readable_cards(hand4.split(' '))
        cards5 = create_readable_cards(hand5.split(' '))
        self.assertEqual(get_score(cards1), 2)
        self.assertNotEqual(get_score(cards2), 2)
        self.assertEqual(get_score(cards3), 2)
        self.assertNotEqual(get_score(cards4), 2)
        self.assertEqual(get_score(cards5), 2)

    def test_play(self):
        all_rounds = [
            '5H 5C 6S 7S KD 2C 3S 8S 8D TD',
            '5D 8C 9S JS AC 2C 5C 7D 8S QH',
            '2D 9C AS AH AC 3D 6D 7D TD QD',
            '4D 6S 9H QH QC 3D 6D 7H QD QS',
            '2H 2D 4C 4D 4S 3C 3D 3S 9S 9D'
        ]
        round1 = ['5H 5C 6S 7S KD 2C 3S 8S 8D TD']
        round2 = ['5D 8C 9S JS AC 2C 5C 7D 8S QH']
        round3 = ['2D 9C AS AH AC 3D 6D 7D TD QD']
        round4 = ['4D 6S 9H QH QC 3D 6D 7H QD QS']
        round5 = ['2H 2D 4C 4D 4S 3C 3D 3S 9S 9D']
        self.assertEqual(play(all_rounds), 3)
        self.assertEqual(play(round1), 0)
        self.assertEqual(play(round2), 1)
        self.assertEqual(play(round3), 0)
        self.assertEqual(play(round4), 1)
        self.assertEqual(play(round5), 1)

    def test_player_1_wins(self):
        filename = os.path.join('files', 'p054_poker.txt')
        rounds = get_rounds(filename)
        player_1_wins = play(rounds)
        self.assertEqual(player_1_wins, 376)


if __name__ == '__main__':
    unittest.main()
