# Find index of rotation point of a list of words

def find_index(ls):
    n = len(ls)
    mid = n/2
    begin = 0
    end = n-1
    while begin < end:
        print end, begin, mid
        if ls[mid] >= ls[begin]:
            begin = mid
        else:
            end = mid
        if end == begin + 1:
            return end
        mid = begin + ((end - begin)/ 2)

words = ['ptolemaic',
         'retrograde',
         'supplant',
         'undulate',
         'xenoepist',
         'asymptote', # <-- rotates here!
         'babka',
         'banoffee',
         'engender',
         'karpatka',
         'othellolagkage']

print find_index(words)
