def rotated_lef(item):
    end = len(item)
    # item[end:end - 1] = item[:1]
    result = item[1:end] + item[:1]
    return result


print('rotated_left: ' + rotated_lef('ABCD'))


def rotated_right(item):
    end = len(item) - 1
    print('last_element: ' + str(item[end: end - 1: -1]))
    result = item[end: end - 1: -1] + item[:end]
    return result


print('rotated_right: ' + rotated_right('BCDA'))