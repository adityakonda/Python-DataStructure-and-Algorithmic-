from util import Util
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


# Data Structure exercise: Stack
# Write a function in python that can reverse a string using stack data structure
def reverse_string1(string):
    stack = Stack()
    cha = ''
    for c in string:
        stack.push(c)

    while not stack.is_empty():
        if not stack.is_empty():
            cha += stack.pop()

    return cha


# using existing deque library.
def reverse_string(string):

    stack = deque()
    reverse_word = ''

    for ch in string:
        stack.append(ch)

    while stack:
        reverse_word += stack.pop()

    return reverse_word


if __name__ == '__main__':

    util = Util()
    print(reverse_string("We will conquere COVID-19"))
    print(reverse_string("tommy"))
    print((reverse_string("he is the king")))







