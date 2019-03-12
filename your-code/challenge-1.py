"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
num_dict_reverse = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}


def calculate(num1, op, num2):
    result = 0

    if num1 not in num_dict.keys() or num2 not in num_dict.keys() or op not in ['plus', 'minus']:
        return "I am not able to answer this question. Check your input."

    if op == 'plus':
        result = num_dict[num1] + num_dict[num2]
    elif op == 'minus':
        result = num_dict[num1] - num_dict[num2]

    if result >= 0:
        return f'{num1} {op} {num2} equals {num_dict_reverse[result]}'
    else:
        return f'{num1} {op} {num2} equals negative {num_dict_reverse[-result]}'


print(calculate(a, b, c))

print("Thanks for using this calculator, goodbye :)")
