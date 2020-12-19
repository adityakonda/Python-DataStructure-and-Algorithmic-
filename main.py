# This is a sample Python script.

# Press ⌃R to execute it or replace it with your codebasics.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from util import Util

def print_hi(name):
    # Use a breakpoint in the codebasics line below to debug your script.
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
    a = util.sortArray([3,2,4,5,1,8])

    a = [[1, 2, 3], [4,5, 6], [7, 8, 9]]

    s = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            s += a[i][j]


    print(s)

    print(util.reverse_string("this is a cat"))

    ab = ["aditya", "thanu", "hari", "ravi"]



    #util.odd_and_even(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
