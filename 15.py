# Compute nth fibonnaci number

# fib(0) # => 0
# fib(1) # => 1
# fib(2) # => 1
# fib(3) # => 2
# fib(4) # => 3

def fib(n):
    ls = [0, 1]
    if n in ls:
        return n
    for i in xrange(2, n+1):
        res = ls[0] + ls[1]
        ls[0] = ls[1]
        ls[1] = res
    return res

# sample run
print fib(1)
print fib(10)
print fib(100)
