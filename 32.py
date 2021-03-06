# You created a game that is more popular than Angry Birds.
# Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest. So far you're using an algorithm that sorts in O(n\lg{n})O(nlgn) time, but players are complaining that their rankings aren't updated fast enough. You need a faster sorting algorithm.


# Write a function that takes:
#
# a list of unsorted_scores
# the highest_possible_score in the game
# and returns a sorted list of scores in less than O(n\lg{n})O(nlgn) time.
#
# For example:
#
#   unsorted_scores = [37, 89, 41, 65, 91, 53]
# HIGHEST_POSSIBLE_SCORE = 100
#
# sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
# # returns [91, 89, 65, 53, 41, 37]
#
# We’re defining n as the number of unsorted_scores because we’re expecting the number of players to keep climbing.
#
# And we'll treat highest_possible_score as a constant instead of factoring it into our big O time and space costs, because the highest possible score isn’t going to change. Even if we do redesign the game a little, the scores will stay around the same order of magnitude.

def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    score_scale = [0] * (HIGHEST_POSSIBLE_SCORE + 1)
    for score in unsorted_scores:
        score_scale[score] += 1

    res = []
    for idx in xrange(HIGHEST_POSSIBLE_SCORE - 1, -1, -1):
        res += [idx] * score_scale[idx]
    return res

unsorted_scores = [37, 89, 41, 65, 91, 53, 90, 90, 90, 90]
HIGHEST_POSSIBLE_SCORE = 100

print sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
