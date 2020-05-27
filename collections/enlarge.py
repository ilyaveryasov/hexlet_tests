def enlarge(items):
    result_list = list()
    for index, item in enumerate(items):
        result_string = ''
        for i in items[index]:
            i = i * 2
            result_string = result_string + i
        result_list.extend([result_string] * 2)
    return result_list
