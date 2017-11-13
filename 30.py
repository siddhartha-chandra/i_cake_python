# Write an efficient function that checks whether any permutation of an input string is a palindrome.
# You can assume the input string only contains lowercase letters.

# Examples:
#
# "civic" should return True
# "ivicc" should return True
# "civil" should return False
# "livci" should return False


def is_potential_palindrome(txt):
    char_set = set()
    for char in txt:
        if char in char_set:
            char_set.remove(char)
        else:
            char_set.add(char)
    return len(char_set) <= 1

examples = ['civic', 'ivicc', 'civil', 'livic']
for example in examples:
    print is_potential_palindrome(example)
