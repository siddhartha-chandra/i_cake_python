# Write a recursive function for generating all permutations of an input string. Return them as a set.
# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.
#
# To start, assume every character in the input string is unique.
#
# Your function can have loops—it just needs to also be recursive.

def get_permutations(text):

    if len(text) <= 1:
        return set([text])

    all_chars_except_last = text[:-1]
    last_char = text[-1]

    permutations_of_all_chars_except_last = get_permutations(
        all_chars_except_last
        )
    
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(permutation_of_all_chars_except_last) + 1):
            permutation = (
                permutation_of_all_chars_except_last[:position] +
                last_char +
                permutation_of_all_chars_except_last[position:]
                )
            permutations.add(permutation)

    return permutations


print get_permutations("cats")
