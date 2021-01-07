from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = 1
        self.right = 2
        pass

def reverse_string(input):
    queue = deque()

    for ch in input:
        queue.append(ch)

    while queue:
        yield queue.pop()



if __name__ == '__main__':
    l = [1,2,2,3,4,5]

    element = [2,3]

    element += [13,12]

    print(element)

    pass

    element.append(1)

    pass
