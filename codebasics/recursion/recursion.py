
# Recursion exercises
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
#ToDo - Exercise
# fibnocci series
0,1,1,2,3,5,8

def fib(n):

    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)


# using iteration
def find_sum_itr(n):
    sum = 0

    for i in range(1, n+1):
        sum = i + sum

    return sum

# using recursion
def find_sum(n):

    if n == 1:
        return 1

    return find_sum(n-1) + n

def list_sum(ls):

    total = 0
    for i in ls:
        total = total + i
    return total


if __name__ == '__main__':
    print(find_sum(4))

    print(fib(3))

    print(list_sum([1,2,3,4]))

    b = list_sum([1,2,3,4])

