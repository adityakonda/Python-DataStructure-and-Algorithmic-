from collections import deque

class Util:

    def fib(self, number):
        a, b = 0, 1
        for i in range(number):
            yield ("{0}: {1}".format(i, a))
            # yield a
            a, b = b, (a + b)

    def prime_number(self, lower, upper):

        print("Prime numbers between", lower, "and", upper, "are:")
        for num in range(lower, upper + 1):
            # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)

    def reverse_string(self, string):

        reverse_string = ''
        stack = deque()

        for c in string:
            stack.append(c)

        i = 0

        while not len(stack) == 0:
            reverse_string += stack.pop()

        return reverse_string


    def reverse_name(self, name):

        i = len(name)

        while i > 0:
            print(name[i - 1], end="")
            i -= 1
        print("\r")

    def pyramid_number(self, number):
        k = 1
        for i in range(number):
            for j in range(i + 1):
                print(k, " ", end="")
                k += 1
            print("\r")

    def pyramid_alphabet(self, number):
        k = 65
        for i in range(number):
            for j in range(i + 1):
                print(chr(k), " ", end="")
            k += 1
            print("\r")

    def odd_and_even(self, number):
        for i in range(1, number+1):
            if i % 2 == 0:
                print(i, "= EVEN number")
            else:
                print(i, "= ODD number")


    def sortArray(self, list):
        existing_list = list
        new_list = []

        while existing_list:
            min = existing_list[0]

            for i in existing_list:
                if i < min:
                    min = i
            
            existing_list.remove(min)
            new_list.append(min)

        return new_list

    def check_grid_is_suduko(self, grid):

        list_number = []

        # check if grid is a sequence
        for x in range(0, 3):
            for y in range(0, 3):
                list_number.append(grid[x][y])

        if sorted(list_number) != [*range(1, 10)]:
            return False
        list_number.clear()

        # check row has duplicated
        for x in range(0, 3):
            for y in range(0, 3):
                list_number.append(grid[x][y])

            if len(list_number) != len(set(list_number)):
                return False
            list_number.clear()

        # check if coln has duplicates
        for y in range(0, 3):
            for x in range(0, 3):
                list_number.append(grid[x][y])

            if len(list_number) != len(set(list_number)):
                return False
            list_number.clear()

        return True

