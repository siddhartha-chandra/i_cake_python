# Given a list of integers, find the highest product you can get
# from three of the integers.

# The input list_of_ints will always have at least three integers

def highest_product(ls):
    print 'running with %s' % ls
    if len(ls) < 3:
        raise Exception('Less than 3 items!')
    highest = max(ls[0], ls[1])
    lowest = min(ls[0], ls[1])
    highest_product_2 = highest * lowest
    lowest_product_2 = highest * lowest
    highest_product = highest_product_2 * ls[2]
    for element in ls[2:]:
        highest_product = max(highest_product, element * lowest_product_2,
                              element * highest_product_2)
        highest_product_2 = max(highest_product_2, element * lowest,
                                element * highest)
        lowest_product_2 = min(lowest_product_2, element * lowest,
                               element * highest)
        highest = max(element, highest)
        lowest = min(element, lowest)
    return highest_product
    
ls = [-10, -10, 1, 3, 2]
print highest_product(ls)
