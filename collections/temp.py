def find_longest_lenght(string):
    result_list = []
    string_list = list(string)
    i = 0
    row = ''
    for index, item in enumerate(string):
        row = row + item
        if string[index] in row:
            result_list.append(string[i: index])
            i = i + 1
    return result_list


print(find_longest_lenght('1234561qweqwer'))
