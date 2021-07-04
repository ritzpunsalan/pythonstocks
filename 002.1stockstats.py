# stockstats.py

# "this is what I'll be investing in."



cmv = " current money value "
""" $500 """
mii = " money invested in "
""" 11 share (much more when the cbp cost is low) """
cbp = " current buy-in price (stock price) "
""" 14.35 ... etc up to $50 to be safe """
gi = " gain increments "
""" (+ 0.03 and higher) """
bi = " bounce increments "
# n = 100

# (/)
""" 
# making the formulas for the division

import numpy as np

for i in np.arange(13.16, 46.76):
    quotient = 500 / i
    print(f"500 divided by {i} is {int(quotient)}.")

this works!!
"""
# cmv = 1500
# mii = 500

# def FunctionName(args):

# if

# else

# if the numbers are not in placed, do not print number set
# else
# null

# print()

# our_set = {x for x in range(1, 101)}
# print(our_set)

print("how much are you invested in webull ?")
print("You currently invested $' + cmv + ' into webull.")
print("what is the buy-in stock cost?")
print("")
print("")
print("")
print("")
print("")
print("")

a = 1

while a == 1:
b = input(“what’s your name?”)
print(“Hi”, b, “, Welcome to Intellipaat!”)


def current_money(cmv):
    cmv = input('How much are you invested in webull?')
    print('You currently invested $' + cmv + ' into webull.')


current_money(cmv)

"""

def multi_table(a):
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))
        print('what is my purpose')


if __name__ == '__main__':
    a = input('Enter a number: ')
    multi_table(float(a))

"""
