from collections import deque


def check_brace(open, close):

    brace_dict = {
        '{': '}',
        '(': ')',
        '[': ']',
    }

    return brace_dict[open] == close


def is_balanced(expression):
    stack = deque()

    for ch in expression:
        if ch == '(' or ch == '{' or ch == '[' or ch == ']' or ch == ')' or ch == '}':

            # if stack is empty & starts with opening braces then stop
            if len(stack) == 0 and (ch == ']' or ch == ')' or ch == '}'):
                return False

            # insert only closed braces
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            # insert only open braces then check_braces then pop elements
            if len(stack) > 0 and (ch == ']' or ch == ')' or ch == '}'):
                return check_brace(stack.pop(), ch)

    return False


if __name__ == '__main__':

    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
