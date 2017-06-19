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

    print "checking ways to make %i with %s" % (amount_left, denominations[current_index:])
    # choose a current coin
    current_coin = denominations[current_index]
    # see how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(amount_left, denominations, current_index + 1)
        amount_left -= current_coin
    return num_possibilities

money = 2
denominations = [1,2,3]
# res = calculate_change(money, sorted(denominations, reverse=True)))
res = change_possibilities_top_down(money, denominations)
print "Number of ways to make change for %s is %s" % (money, res)
