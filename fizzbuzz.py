def fizz_buzz(number, dictionary):
    dict_keys = dictionary.keys()
    dict_keys.sort(reverse=True)
    for k in dict_keys:
        if number%k == 0:
            return dictionary[k]
    return number


dictionary = {3: 'Fizz', 5: 'Buzz', 15: 'FizzBuzz', 17: 'Jazz'}
a = range(1,101)
res = map(lambda x: fizz_buzz(x, dictionary), a)
print res
