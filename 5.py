# Write a function that, given:
#
# an amount of money
# a list of coin denominations
# computes the number of ways to make amount of money with coins of the
# available denominations.

# Example: for amount=4 and denominations=[1,2,3],
# your program would output 4: the number of ways to make 4 cents
# with those denominations:
#
# 1c, 1c, 1c, 1c
# 1c, 1c, 2c
# 1c, 3c
# 2c, 2c

# Approach 1: naive approach (self)
def is_change_possible(count):
    if count is 0:
        return 1
    else:
        return 0

def calculate_change(money, denominations):
    check = is_change_possible(money)
    if len(denominations) is 0:
        return check
    elif money < 0:
        return 0
    else:
        return (calculate_change(money - denominations[0], denominations) +
                calculate_change(money, denominations[1:]))

# Approach 2: top-down without memoization (icake)
def change_possibilities_top_down(amount_left, denominations, current_index=0):
    #base cases:
    # we got the exact amount
    if amount_left is 0:
        return 1
    # we overshot the amount`
    if amount_left <0:
        return 0
    # out of denominations
    if current_index == len(denominations):
        return 0

    print "checking ways to make %i with %s" % (amount_left,
                                                denominations[current_index:])
    # choose a current coin
    current_coin = denominations[current_index]
    # see how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(amount_left,
                                                           denominations,
                                                           current_index + 1)
        amount_left -= current_coin
    return num_possibilities



# Approach 3: top-down with memoization(icake)

class Change:
    def __init__(self):
        self.memo = {}

    def change_possibilities_top_down(self,
                                      amount_left,
                                      denominations,
                                      current_index=0):
        memo_key = str((amount_left, current_index))
        if memo_key in self.memo:
            print "Grabbing memo[%s]" % memo_key
            return self.memo[memo_key]

        # base cases
        # we hit the amount spot on. yes!
        if amount_left == 0:
            print 'yay!\n'
            return 1

        # we overshot the amount left (used too many coins)
        if amount_left < 0:
            print 'overshot! :(\n'
            return 0

        # we're out of denominations
        if current_index == len(denominations):
            print 'no more coins :(\n'
            return 0

        print "checking ways to make %i with %s" % (amount_left,
                                                    denominations[
                                                        current_index:
                                                        ]
                                                    )
        # choose a current coin
        current_coin = denominations[current_index]

        num_possibilities = 0
        while amount_left >= 0:
            num_possibilities += (
                self.change_possibilities_top_down(
                    amount_left, denominations, current_index + 1
                    )
                )
            amount_left -= current_coin
        self.memo[memo_key] = num_possibilities
        return num_possibilities


# Approach 4: bottom-up
def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1
    for coin in denominations:
        for higher_amount in xrange(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
    return ways_of_doing_n_cents[amount]


money = 5
denominations = [1,3,5]
# res = calculate_change(money, sorted(denominations, reverse=True)))
# res = change_possibilities_top_down(money, denominations)
# res = Change().change_possibilities_top_down(money, denominations)
res = change_possibilities_bottom_up(money, denominations)
print "Number of ways to make change for %s is %s" % (money, res)
