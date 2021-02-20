# https://leetcode.com/problems/palindrome-number/

from collections import deque

class Solution:

    def isPalindrome(self, x):

        reverse = ''
        stack = deque()
        for ch in str(x):
            stack.append(ch)

        while stack:
            reverse += stack.pop()

        if str(x) == reverse:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("mom"))