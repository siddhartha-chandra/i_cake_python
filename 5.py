# Write a function that, given:
#
# an amount of money
# a list of coin denominations
# computes the number of ways to make amount of money with coins of the
# available denominations.

# Example: for amount=4 and denominations=[1,2,3],
# your program would output 4—the number of ways to make 4¢
# with those denominations:
#
# 1¢, 1¢, 1¢, 1¢
# 1¢, 1¢, 2¢
# 1¢, 3¢
# 2¢, 2¢

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

money = 2
denominations = [3]
print ("Number of ways to make change for %s is %s"
       % (money, calculate_change(money, sorted(denominations, reverse=True))))
