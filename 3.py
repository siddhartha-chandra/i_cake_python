# Given a list of integers, find the highest product you can get
# from three of the integers.

# The input list_of_ints will always have at least three integers

def get_min(a, b):
    if a is None:
        return b
    elif b is None:
        return a
    else:
        min(a, b)

def place_element_and_calculate(element):
    global highest, lowest, lowest_product_2, highest_product_2, highest_product
    if highest is None:
        highest = element
    elif lowest is None:
        highest_product_2 = highest * element
        lowest = min(highest, element)
        highest = max(highest, element)
    else:
        if highest_product is None:
            highest_product = element * highest_product_2
        elif element * highest_product_2 > highest_product:
            lowest_product_2 = get_min(highest_product_2, lowest_product_2)
            highest_product = element * highest_product_2
            highest_product_2 = max(highest_product_2, element * highest)
            lowest = min(lowest, highest)
            highest = max(element, highest)
        else:
            if element * lowest > highest_product_2:
                lowest_product_2 = get_min(highest_product_2, lowest_product_2)
                highest_product_2 = element * lowest
                highest_product = highest * highest_product_2
            else:
                lowest_product_2 = element * lowest
            lowest = min(lowest, element)

def my_function(ls):
    print 'running with %s' % ls
    for element in ls:
        place_element_and_calculate(element)
    return highest_product


# run your function through some test cases here
# remember: debugging is half the battle!
highest = None
lowest = None
highest_product_2 = None
lowest_product_2 = None
highest_product = None
ls = [-10, -10, 1, 3, 2]
print my_function(ls)
