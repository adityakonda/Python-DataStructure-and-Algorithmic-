import string

data = sorted(input("Please input data: "))

low_case = list(filter(lambda x: x in string.ascii_lowercase, data))
upper_case = list(filter(lambda x: x in string.ascii_uppercase, data))
digits = list(filter(lambda x: x in string.digits, data))
special_char = list(filter(lambda x: x not in string.ascii_lowercase and x not in string.ascii_uppercase and x not in string.digits, data))

odd = list(filter(lambda x: int(x) % 2 != 0, digits))
even = list(filter(lambda x: int(x) % 2 == 0, digits))

result = set(low_case + upper_case + odd + even + special_char)

print(*result, sep=",")

