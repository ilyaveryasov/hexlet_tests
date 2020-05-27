def pre_string(string):
    row = string[0]
    for item in string[1:]:
        if item in row:
            return row
        else:
            row += item
    return row


def find_max_lenght(string):
    result1 = 0
    i = 0
    while i < len(string):
        if len(pre_string(string[i:])) > result1:
            result1 = len(pre_string(string[i:]))
        else:
            result1 = result1
        i += 1
    return result1


string = '1234561qweqwer'
print(find_max_lenght(string))
