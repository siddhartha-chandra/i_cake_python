# Find a duplicate, Space Edition™.
# We have a list of integers, where:
#
# The integers are in the range 1..n1..n
# The list has a length of n+1n+1
# It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.
#
# Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)
#
# We're going to run this function on our new, super-hip Macbook Pro With Retina Display™. Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't upgrade our RAM. So we need to optimize for space!

# time: o(n); space: o(n)
def find_repeat_naive(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)

    # whoops--no duplicate
    raise Exception('no duplicate!')

def find_repeat_brute_force(numbers):
    for needle in range(1, len(numbers)):
        has_been_seen = False
        for number in numbers:
            if number == needle:
                if has_been_seen:
                    return number
                else:
                    has_been_seen = True

    # whoops--no duplicate
    raise Exception('no duplicate!')


# Solution

# Our approach is similar to a binary search, except we divide the range of possible answers in half at each step, rather than dividing the list in half.
#
# 1. Find the number of integers in our input list which lie within the range 1..n/2
# 2. Compare that to the number of possible unique integers in the same range.
# 3. If the number of actual integers is greater than the number of possible integers, we know there’s a duplicate in the range 1..n/2, so we iteratively use the same approach on that range.
# 4. If the number of actual integers is not greater than the number of possible integers, we know there must be duplicate in the range n/2 + 1..n, so we iteratively use the same approach on that range.
# 5. At some point our range will contain just 1 integer, which will be our answer.

def find_repeat(the_list):
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:

        # divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # lower range is floor..midpoint
        # upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) / 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = \
            lower_range_ceiling - lower_range_floor + 1

        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # there must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # there must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # floor and ceiling have converged
    # we found a number that repeats!
    return floor


# Complexity
# O(1)O(1) space and O(n\lg{n})O(nlgn) time.
#
# Tricky as this solution is, we can actually do even better, getting our runtime down to O(n)O(n) while keeping our space cost at O(1)O(1). The solution is NUTS; it's probably outside the scope of what most interviewers would expect. But for the curious...here it is!
#
# Bonus
# This function always returns one duplicate, but there may be several duplicates. Write a function that returns all duplicates.
#
# What We Learned
# Our answer was a modified binary search. We got there by reasoning about the expected runtime:
#
# We started with an O(n^2)O(n
# ​2
# ​​ ) "brute force" solution and wondered if we could do better.
# We knew to beat O(n^2)O(n
# ​2
# ​​ ) we'd probably do O(n)O(n) or O(n\lg{n})O(nlgn), so we started thinking of ways we might get an O(n\lg{n})O(nlgn) runtime.
# \lg{(n)}lg(n) usually comes from iteratively cutting stuff in half, so we arrived at the final algorithm by exploring that idea.
# Starting with a target runtime and working backwards from there can be a powerful strategy for all kinds of coding interview questions.
