
# Check how to use lambda function
# https://www.hackerrank.com/rest/contests/master/challenges/ginorts/hackers/lambdalala/download_solution?primary=true

import string


def func(input):

    input = sorted(input)
    output = ""

    for ch in input:
        if ch in string.ascii_lowercase:
            output += ch

    for ch in input:
        if ch in string.ascii_uppercase:
            output += ch

    for ch in input:
        if ch in string.digits and int(ch) % 2 != 0:
            output += ch

    for ch in input:
        if ch in string.digits and int(ch) % 2 == 0:
            output += ch

    return output


if __name__ == '__main__':

    print(func("Kaditya1234"))

    input_val = input("please enter :")
    print("--> ", input_val)



