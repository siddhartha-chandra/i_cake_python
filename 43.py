# In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.
#
# Each order is represented by an "order id" (an integer).
#
# We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.
#
# For example:
# my_list     = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]
#
# print merge_lists(my_list, alices_list)
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]


def merge_lists(my_list, alices_list):
    my_list_length = len(my_list)
    alices_list_length = len(alices_list)
    my_list_ptr = 0
    alices_list_ptr = 0
    merged_list_size = my_list_length + alices_list_length
    merged_list = [None] * merged_list_size
    for i in range(my_list_length + alices_list_length):
        if my_list_ptr < my_list_length and alices_list_ptr < alices_list_length:
            if my_list[my_list_ptr] <= alices_list[alices_list_ptr]:
                merged_list[i] = my_list[my_list_ptr]
                my_list_ptr += 1
            else:
                merged_list[i] = alices_list[alices_list_ptr]
                alices_list_ptr += 1
        elif my_list_ptr < my_list_length:
            merged_list[i] = my_list[my_list_ptr]
            my_list_ptr += 1
        else:
            merged_list[i] = alices_list[alices_list_ptr]
            alices_list_ptr += 1
    return merged_list

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_lists(my_list, alices_list)
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]


# Complexity
# O(n) time and O(n) additional space, where nn is the number of items in the merged list.
#
# The added space comes from allocating the merged_list. There's no way to do this " in-place" because neither of our input lists are necessarily big enough to hold the merged list.
#
# But if our inputs were linked lists, we could avoid allocating a new structure and do the merge by simply adjusting the next pointers in the list nodes!
#
# In our implementation above, we could avoid tracking current_index_merged and just compute it on the fly by adding current_index_mine and current_index_alices. This would only save us one integer of space though, which is hardly anything. It's probably not worth the added code complexity.
#
# Trivia! Python's native sorting algorithm is called Timsort. It's actually optimized for sorting lists where subsections of the lists are already sorted. For this reason, a more naive algorithm:

#   def merge_sorted_lists(arr1, arr2):
#     return sorted(arr1 + arr2)

# Python
# is actually faster until nn gets pretty big. Like 1,000,000.
#
# Also, in Python 2.6+, there's a built-in function for merging sorted lists into one sorted list: heapq.merge().

# Bonus
# What if we wanted to merge several sorted lists? Write a function that takes as an input a list of sorted lists and outputs a single sorted list with all the items from each list.

# Do we absolutely have to allocate a new list to use for the merged output? Where else could we store our merged list? How would our function need to change?

# What We Learned
# We spent a lot of time figuring out how to cleanly handle edge cases.

# Sometimes it's easy to lose steam at the end of a coding interview when you're debugging. But keep sprinting through to the finish! Think about edge cases. Look for off-by-one errors.
