import datetime

format_string = "%a %d %b %Y %H:%M:%S %z"
T = int(input("t input"))

for test in range(T):
    t1 = str(input("t1 time"))
    t2 = str(input("t2 time"))

    parsed_t1 = datetime.datetime.strptime(t1, format_string)
    parsed_t2 = datetime.datetime.strptime(t2, format_string)

    diff = parsed_t2 - parsed_t1

    print (abs(int((diff.total_seconds()))))