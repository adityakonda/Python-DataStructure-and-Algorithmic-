import re

if __name__ == '__main__':

    #pattern = "^a...s$" # start with 'a' and ends with 's'. Between 'a' and 's' there must be three characters
    pattern = "[0-9-]"
    input_string = "2342-AD-23423"

    if re.match(pattern, input_string):
        print("matched")
        print(re.findall(pattern, input_string))
    else:
        print("not matched")

