# 1.    preliminary condition
condition = True

if condition:
    x = 1
else:
    x = 0

# preliminary condition
x = 1 if condition else 0

print(x)

# 2.    _ is used as seperators
num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(f'{total:,}')

# 3.    Context Manager: Used for managing resources -- For more info refer the additional link

# without context manager
f = open('/Users/kondaaditya/Documents/test.txt', 'r')
file_contexts_test = f.read()
f.close()

# with context manager:
with open('/Users/kondaaditya/Documents/test.txt', 'r') as f:
    file_contexts = f.read()

words = file_contexts.split(' ')
word_count = len(words)
print(word_count)

# 4.    enumerate: function return both the index & values

name = ['apple', 'orange', 'strawberry', 'mango']

for index, name in enumerate(name, start=1):
    print(index, name)


