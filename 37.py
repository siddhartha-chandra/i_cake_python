# You have a function rand7() that generates a random integer from 1 to 7. Use it to write a function rand5() that generates a random integer from 1 to 5.

# rand7() returns each integer with equal probability. rand5() must also return each integer with equal probability.


def rand5():
    result = 7  # arbitrarily large
    while result > 5:
        result = rand7()
    return result

def rand5():
    roll = rand7()
    return roll if roll <= 5 else rand5()


# Bonus
# This kind of math is generally outside the scope of a coding interview, but: if you know a bit of number theory you can prove that there exists no solution which is guaranteed to terminate. Hint: it follows from the fundamental theorem of arithmetic. ↴
