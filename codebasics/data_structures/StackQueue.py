from codebasics.data_structures.Stack import Stack
from util import Util


# Data Structure exercise: Stack
# Write a function in python that can reverse a string using stack data structure
def reverse_string(string):
    stack = Stack()
    cha = ''
    for c in string:
        stack.push(c)

    while not stack.is_empty():
        if not stack.is_empty():
            cha += stack.pop()

    return cha


if __name__ == '__main__':

    util = Util()
    print(reverse_string("We will conquere COVID-19"))
    print((util.reverse_string("he is the king")))







