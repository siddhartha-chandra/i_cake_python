# write a program that prints the numbers from 1 to 100. But for multiples of 3 print ‘Fizz’ instead of the number and for the multiples of 5 print ‘Buzz’. For numbers which are multiples of both 3 and 5 print ‘FizzBuzz’

def fizz_buzz(ls, dictionary):
    dict_keys = dictionary.keys()
    dict_keys.sort(reverse=True)

    def fizz_buzz_number(number):
        for k in dict_keys:
            if number%k == 0:
                return dictionary[k]
        return number

    return [fizz_buzz_number(k) for k in ls]


dictionary = {3: 'Fizz', 5: 'Buzz', 15: 'FizzBuzz', 17: 'Jazz'}
a = range(1,101)
res = fizz_buzz(a, dictionary)
print res
