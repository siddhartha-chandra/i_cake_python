# You're working with an intern that keeps coming to you with JavaScript code that won't run because the braces, brackets, and parentheses are off. To save you both some time, you decide to write a braces/brackets/parentheses validator.
# Let's say:
#
# '(', '{', '[' are called "openers."
# ')', '}', ']' are called "closers."
# Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.
#
# Examples:
#
# "{ [ ] ( ) }" should return True
# "{ [ ( ] ) }" should return False
# "{ [ }" should return False

def is_balanced(txt):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for ch in txt:
        if ch in brackets.keys():
            print 'appending!'
            print stack
            stack.append(ch)
            print stack
            print ' ----- '
        elif ch in brackets.values():
            if not stack:
                print 'not balanced!'
                print stack
                return False
            else:
                last_unclosed_pair = stack.pop()
                if not brackets[last_unclosed_pair] == ch:
                    return False
    return stack == []

ex_1 = "{ [ ] ( ) }"
ex_2 = "{ [ ( ] ) }"
ex_3 = "{ [ }"
ex_4 = "{ [ ( ] ) }"
is_balanced(ex_1)
