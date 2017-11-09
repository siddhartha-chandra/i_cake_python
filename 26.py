# Write a function to reverse a string in-place

def reverse_in_place(txt):
    txt_list = list(txt)
    length = len(txt)

    for i in xrange(length/2):
        tmp = txt_list[length - i - 1]
        txt_list[length - i - 1] = txt_list[i]
        txt_list[i] = tmp
    return ''.join(txt_list)

def reverse_ic(string):
    string_list = list(string)
    left_pointer  = 0
    right_pointer = len(string_list) - 1

    while left_pointer < right_pointer:

        # swap characters
        string_list[left_pointer], string_list[right_pointer] = \
            string_list[right_pointer], string_list[left_pointer]

        # move towards middle
        left_pointer  += 1
        right_pointer -= 1

    return ''.join(string_list)

a = "hello"
reverse_in_place(a)
reverse_ic(a)
