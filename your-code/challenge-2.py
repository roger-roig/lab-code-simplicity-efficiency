"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

import random
import string
import sys

characters = string.ascii_lowercase + string.digits


def random_string_generator(length, char_seq):
    result_string = ''
    for i in range(length):
        result_string += random.choice(char_seq)
    return result_string


def batch_string_generator(str_num, min_len=8, max_len=12):
    string_list = []
    for i in range(str_num):
        if min_len < max_len:
            c = random.choice(range(min_len, max_len+1))
        elif min_len == max_len:
            c = min_len
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        string_list.append(random_string_generator(c, characters))
    return string_list


a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

if a not in string.digits or b not in string.digits or n not in string.digits:
    sys.exit('Incorrect input. Please try again.')

print(batch_string_generator(int(n), int(a), int(b)))
