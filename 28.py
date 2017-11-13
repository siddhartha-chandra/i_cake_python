# I like parentheticals (a lot).
# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
#
# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.
#
# Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).


def parenthesis_finder(txt, index):
    if not txt[index] == '(':
        raise Exception("index does not correspond to a parenthesis!")
    parenthesis_count = 0
    position = index + 1
    while position <= len(txt) - 1:
        if txt[position] == ')':
            if parenthesis_count == 0:
                return position
            else:
                print ('Found parenthesis, but not companion')
                parenthesis_count -= 1
        elif txt[position] == '(':
            parenthesis_count += 1
        position += 1
    raise Exception("Companion parenthesis not found :( ")



text = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
parenthesis_finder(text, 10)
