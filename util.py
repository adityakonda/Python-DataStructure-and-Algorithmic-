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


