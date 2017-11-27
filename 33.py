# I have a list of n + 1 numbers. Every number in the range 1..n1..n appears once except for one number that appears twice.
# Write a function for finding the number that appears twice.

def number_that_appaears_twice(ls):
    ls_sum = sum(ls)
    n = max(ls)
    series_sum = n * (n + 1) / 2
    return ls_sum - series_sum

sample = [1,4,6,2,4,3,5]
number_that_appaears_twice(sample)
