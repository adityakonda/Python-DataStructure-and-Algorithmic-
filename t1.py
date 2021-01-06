from collections import deque


def reverse_string(input):
    queue = deque()

    for ch in input:
        queue.append(ch)

    while queue:
        yield queue.pop()


if __name__ == '__main__':
    l = [1,2,2,3,4,5]
    if l:
        print("hi")
    pass
