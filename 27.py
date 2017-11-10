# You're working on a secret team solving coded transmissions

# Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault. The message has been mostly deciphered, but all the words are backwards! Your colleagues have handed off the last step to you.
#
# Write a function reverse_words() that takes a string message and reverses the order of the words in-place.

# When writing your function, assume the message contains only letters and spaces, and all words are separated by one space.

def reverse_words(txt):
    ls = txt.split()
    length = len(ls)

    left_ptr = 0
    right_ptr = length - 1

    while left_ptr < right_ptr:
        ls[left_ptr], ls[right_ptr] = ls[right_ptr], ls[left_ptr]
        left_ptr += 1
        right_ptr -= 1

    return ' '.join(ls)


def reverse_ic(msg_list, left_index, right_index):
    while left_index < right_index:

        # swap characters
        msg_list[left_index], msg_list[right_index] = \
            msg_list[right_index], msg_list[left_index]

        # move towards middle
        left_index  += 1
        right_index -= 1

    return msg_list


def reverse_words_ic(txt):
    ls = list(txt)
    length = len(txt)
    last_index = length - 1
    reverse_ls = reverse_ic(ls, 0, last_index)
    begin_index = 0
    for end_index in xrange(length + 1):
        if end_index == length or reverse_ls[end_index] == ' ':
            # print "%s" % reverse_ls[begin_index:end_index]
            reverse_ic(reverse_ls, begin_index, end_index - 1)
            # print "%s" % reverse_ls[begin_index:end_index]
            begin_index = end_index + 1

    return ''.join(reverse_ls)


message = 'find you will pain only go you recordings security the into if'
reverse_words_ic(message)
# returns: 'if into the security recordings you go only pain will you find'
