# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from util import Util

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def a(num):

    for i in range(num+1):
        for j in range(i):
            print("* ", end="")
        print("\r")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


    util = Util()
    util.reverse_name("aditya")
    util.odd_and_even(10)
    #util.pyramid_alphabet(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
