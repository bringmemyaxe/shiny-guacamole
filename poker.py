import itertools
import sys
from collections import defaultdict

# Define the payouts for each hand
PAYOUTS = {
    'jacks_or_better': 1,
    'two_pairs': 2,
    'three_of_a_kind': 3,
    'straight': 4,
    'flush': 6,
    'full_house': 9,
    'four_of_a_kind': 25,
    'straight_flush': 50,
    'royal_flush': 800
}

# Define the ranks and suits
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['C', 'D', 'H', 'S']

# Generate all possible cards
ALL_CARDS = [rank + suit for rank in RANKS for suit in SUITS]

def progressbar(value, endvalue):
    percent = float(value) / endvalue
    sys.stdout.write("\r{0}% is done… Wait…".format(int(round(percent * 100))))
    sys.stdout.flush()

def check_hand(hand):
    ranks = [card[:-1] for card in hand]
    suits = [card[-1] for card in hand]
    rank_counts = defaultdict(int)
    for rank in ranks:
        rank_counts[rank] += 1
    suit_counts = defaultdict(int)
    for suit in suits:
        suit_counts[suit] += 1
    
    # Check for Royal Flush
    if set(ranks) == set(['10', 'J', 'Q', 'K', 'A']) and len(suit_counts) == 1:
        return 'royal_flush', PAYOUTS['royal_flush']
    
    # Check for Straight Flush
    sorted_ranks = sorted(ranks, key=lambda x: RANKS.index(x))
    if len(set(suits)) == 1 and is_straight(sorted_ranks):
        return 'straight_flush', PAYOUTS['straight_flush']
    
    # Check for Four of a Kind
    if 4 in rank_counts.values():
        return 'four_of_a_kind', PAYOUTS['four_of_a_kind']
    
    # Check for Full House
    if 3 in rank_counts.values() and 2 in rank_counts.values():
        return 'full_house', PAYOUTS['full_house']
    
    # Check for Flush
    if len(set(suits)) == 1:
        return 'flush', PAYOUTS['flush']
    
    # Check for Straight
    if is_straight(sorted_ranks):
        return 'straight', PAYOUTS['straight']
    
    # Check for Three of a Kind
    if 3 in rank_counts.values():
        return 'three_of_a_kind', PAYOUTS['three_of_a_kind']
    
    # Check for Two Pairs
    if list(rank_counts.values()).count(2) == 2:
        return 'two_pairs', PAYOUTS['two_pairs']
    
    # Check for Jacks or Better
    for rank in ['J', 'Q', 'K', 'A']:
        if rank_counts[rank] == 2:
            return 'jacks_or_better', PAYOUTS['jacks_or_better']
    
    return 'none', 0

def is_straight(sorted_ranks):
    # Check for a straight
    return all(RANKS.index(sorted_ranks[i]) == RANKS.index(sorted_ranks[i-1]) + 1 for i in range(1, len(sorted_ranks)))

def compute_expected_value(hand, held_indices):
    remaining_cards = [card for card in ALL_CARDS if card not in hand]
    total_combinations = 0
    total_payout = 0
    
    for new_cards in itertools.combinations(remaining_cards, 5 - len(held_indices)):
        new_hand = [hand[i] for i in held_indices] + list(new_cards)
        hand_type, payout = check_hand(new_hand)
        total_payout += payout
        total_combinations += 1
    
    return total_payout / total_combinations if total_combinations else 0

def main():
    your_cards = []
    while len(your_cards) < 5:
        card = input(f'INPUT YOUR {len(your_cards) + 1} CARD: ')
        if card in ALL_CARDS and card not in your_cards:
            your_cards.append(card)
        else:
            print("Invalid card or card already chosen. Try again.")
    
    results = {}
    for i in range(32):
        held_indices = [j for j in range(5) if i & (1 << j)]
        expected_value = compute_expected_value(your_cards, held_indices)
        results[tuple(held_indices)] = expected_value
    
    print("\nThese are the best options, as you can see:")
    for held_indices, expected_value in sorted(results.items(), key=lambda x: -x[1]):
        held_str = ''.join('T' if i in held_indices else 'F' for i in range(5))
        print(f"If you change {held_str}: {expected_value:.10f}$")

if __name__ == "__main__":
    main()
