# https://leetcode.com/problems/reverse-integer/
from collections import deque


class Solution:

    def reverse(self, x):

        result = ''
        stack = deque()

        for i in str(x):
            if i.isdigit():
                stack.append(i)

        while stack:
            result += stack.pop()

        if x < 0:
            return - int(result)

        return int(result)


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-234))