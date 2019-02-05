# Solution to Poker hands, problem 54 of Project Euler:
# https://projecteuler.net/problem=54


import os
import time


CARD_TO_VALUE = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
    '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1
}

start = time.time()


def get_rounds(filename):
    with open(filename) as f:
        lines = f.read()
    rounds = lines.strip().split('\n')
    return rounds


def play(rounds):
    player1_wins = 0
    for single_round in rounds:

        # get card values
        single_round = single_round.split(' ')
        player1_hand = create_readable_cards(single_round[:5])
        player2_hand = create_readable_cards(single_round[5:])

        # get scores
        player1_score = get_score(player1_hand)
        player2_score = get_score(player2_hand)

        # determine winner
        if player1_score > player2_score:
            player1_wins += 1
        elif player1_score == player2_score:
            player1_pairs = get_pairs(player1_hand, 2)
            player2_pairs = get_pairs(player2_hand, 2)
            # if pairs - check for three of a kind
            if player1_pairs['pair_count'] or player2_pairs['pair_count']:
                player_1_three = get_pairs(player1_hand, 3)
                player_2_three = get_pairs(player2_hand, 3)
                # if three of a kind
                if player_1_three['pair_count']:
                    if player_2_three['pairs'][-1]:
                        if player_1_three['pairs'][-1] > player_2_three['pairs'][-1]:
                            player1_wins += 1
                    else:
                        player1_wins += 1
                # compare highest pairs
                if player1_pairs['pairs'][-1] > player2_pairs['pairs'][-1]:
                    player1_wins += 1
                # if pairs are equal, compare highest remaining cards
                if player1_pairs['pairs'][-1] == player2_pairs['pairs'][-1]:
                    player1_remaining_cards = list(
                        set(player1_hand['cards']) - set(player1_pairs['pairs']))
                    player2_remaining_cards = list(
                        set(player2_hand['cards']) - set(player2_pairs['pairs']))
                    if sorted(player1_remaining_cards)[-1] > sorted(player2_remaining_cards)[-1]:
                        player1_wins += 1
            # if no pairs - compare highest cards
            else:
                if player1_hand['cards'][4] > player2_hand['cards'][4]:
                    player1_wins += 1

    return player1_wins


def create_readable_cards(hand):
    """Given a hand, returns a dict of sorted cards (as values) and suits

    Arguments:
      hand (list of str): Description of arg1

    Returns:
      A dict of sorted cards (mapping card name to value) and suits

    Example:
      >>> print(create_readable_cards(['7C', '8C', '5C', 'QD', '6C']))
      {'cards': [5, 6, 7, 8, 12], 'suits': ['C', 'C', 'C', 'D', 'C']}
    """

    cards = []
    suits = []
    for card in hand:
        value = CARD_TO_VALUE[card[0]]
        cards.append(value)
        suits.append(card[1])
    return {
      'cards': sorted(cards),
      'suits': suits
    }


def check_if_same_suit(suits):
    return all(suit == suits[0] for suit in suits)


def get_score(hand):
    score = 1
    while True:
        if check_royal_flush(hand):
            score = 10
            break
        if check_straight_flush(hand):
            score = 9
            break
        if check_four_of_a_kind(hand):
            score = 8
            break
        if check_full_house(hand):
            score = 7
            break
        if check_if_same_suit(hand['suits']):
            score = 6
            break
        if check_straight(hand):
            score = 5
            break
        if check_three_of_a_kind(hand):
            score = 4
            break
        if check_two_pairs(hand):
            score = 3
            break
        if check_one_pair(hand):
            score = 2
            break
        break
    return score


# helpers for checking hands

def check_royal_flush(hand):
    cards = set(hand['cards'])
    check_royal_flush_set = set([10, 11, 12, 13, 14])
    if cards == check_royal_flush_set and check_if_same_suit(hand['suits']):
        return True
    return False


def check_straight_flush(hand):
    if not check_if_same_suit(hand['suits']):
        return False
    return check_straight(hand)


def check_four_of_a_kind(hand):
    return hand['cards'][0] == hand['cards'][3] or \
           hand['cards'][1] == hand['cards'][4]


def check_three_of_a_kind(hand):
    return hand['cards'][0] == hand['cards'][2] or \
           hand['cards'][1] == hand['cards'][3] or \
           hand['cards'][2] == hand['cards'][4]


def check_two_pairs(hand):
    pairs = get_pairs(hand, 2)
    if pairs['pair_count'] == 2:
        return True
    return False


def check_full_house(hand):
    if check_three_of_a_kind(hand) and check_two_pairs(hand):
        return True
    return False


def check_straight(hand):
    length = len(hand['cards'])
    results = True
    for i in range(length):
        if i + 1 < length:
            if hand['cards'][i+1] - hand['cards'][i] != 1:
                results = False
                return results
    return results


def check_one_pair(hand):
    pairs = get_pairs(hand, 2)
    if pairs['pair_count'] == 1:
        return True
    return False


def get_pairs(hand, num_pairs):
    pair_count = 0
    pairs = []
    for card in hand['cards']:
        if hand['cards'].count(card) >= num_pairs and card not in pairs:
            pair_count += 1
            pairs.append(card)
    return {
        'pair_count': pair_count,
        'pairs': pairs
    }


def main():
    filename = os.path.join('files', 'p054_poker.txt')
    # filename = os.path.join('files', 'single_round.txt')
    rounds = get_rounds(filename)
    player_1_wins = play(rounds)
    print(f'Player 1 wins - {player_1_wins}')
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
