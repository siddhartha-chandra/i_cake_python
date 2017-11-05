from math import sqrt

# Compute nth fibonnaci number

# fib(0) # => 0
# fib(1) # => 1
# fib(2) # => 1
# fib(3) # => 2
# fib(4) # => 3
# todo: find answer in o(log(n))
def fib(n):
    ls = [0, 1]
    if n in ls:
        return n
    for i in xrange(2, n+1):
        res = ls[0] + ls[1]
        ls[0] = ls[1]
        ls[1] = res
    return res

# complexity: O(1) using Binet's formula
def fib_o_1(n):
    t1 = (float(1 + sqrt(5))/2) ** n
    t2 = (float(1 - sqrt(5))/2) ** n
    res = (1/sqrt(5)) * (t1-t2)
    return res


# sample run
print fib(1)
print fib(10)
print fib(100)

# sample run
print ("Running in Constant time now:")
print fib_o_1(1)
print fib_o_1(10)
print fib_o_1(100)
