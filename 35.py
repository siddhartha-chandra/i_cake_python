# Write a function for doing an in-place shuffle of a list.
# The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.
#
# Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.


import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(the_list):
    # if it's 1 or 0 items, just return
    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    # walk through from beginning to end
    for index_we_are_choosing_for in xrange(0, len(the_list) - 1):

        # choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # must be an item AFTER the current item, because the stuff
        # before has all already been placed
        random_choice_index = get_random(index_we_are_choosing_for,
                                         last_index_in_the_list)

        # place our random choice in the spot by swapping
        if random_choice_index != index_we_are_choosing_for:
            the_list[index_we_are_choosing_for], the_list[random_choice_index] = \
                the_list[random_choice_index], the_list[index_we_are_choosing_for]

# This is a semi-famous algorithm known as the Fisher-Yates shuffle (sometimes called the Knuth shuffle).
#
# Complexity
# O(n)O(n) time and O(1)O(1) space.
