# You have a function rand5() that generates a random integer from 1 to 5. Use it to write a function rand7() that generates a random integer from 1 to 7.
# rand5() returns each integer with equal probability. rand7() must also return each integer with equal probability.

def rand7_table():
    results = [1, 2, 3, 4 , 5, 6, 7]

    while True:

        # do our die rolls
        # do our die rolls
        roll1 = rand5()
        roll2 = rand5()

        outcome_number = (roll1-1) * 5 + (roll2-1) + 1

        # case: we hit an extraneous outcome
        # so we need to re-roll
        if outcome_number > 21:
            continue

        # our outcome was fine. return it!
        idx = outcome_number % 7 + 1
        return results[idx]
