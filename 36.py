# I figured out how to get rich: online poker.
# I suspect the online poker game I'm playing shuffles cards by doing a single riffle.
#
# To prove this, let's write a function to tell us if a full deck of cards shuffled_deck is a single riffle of two other halves half1 and half2.
#
# We'll represent a stack of cards as a list of integers in the range 1..521..52 (since there are 5252 distinct cards in a deck).
# Why do I care? A single riffle is not a completely random shuffle. If I'm right, I can make more informed bets and get rich and finally prove to my ex that I am not a "loser with an unhealthy cake obsession" (even though it's too late now because she let me go and she's never getting me back).


def is_single_riffle(shuffled_deck, half1, half2):
    assert(len(half1) + len(half2) == len(shuffled_deck))
    half1_idx = 0
    half2_idx = 0
    half1_max_idx = len(half1) - 1
    half2_max_idx = len(half2) - 1

    for card in shuffled_deck:
        if half1_idx <= half1_max_idx and card == half1[half1_idx]:
            half1_idx += 1
        elif half2_idx <= half2_max_idx and card == half2[half2_idx]:
            half2_idx += 1
        else:
            return False
    return True

deck = [1,2,3,4,5,6]
h_1 = [4,5,6]
h_2 = [1,2,3]
is_single_riffle(deck, h_1, h_2)


# Bonus
# This assumes shuffled_deck contains all 52 cards. What if we can't trust this (e.g. some cards are being secretly removed by the shuffle)?
# This assumes each number in shuffled_deck is unique. How can we adapt this to rifling lists of random integers with potential repeats?
# Our solution returns True if you just cut the deck—take one half and put it on top of the other. While that technically meets the definition of a riffle, what if you wanted to ensure that some mixing of the two halves occurred?
