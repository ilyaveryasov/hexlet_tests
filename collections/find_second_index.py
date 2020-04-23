def find_index(value, items):
    for (index, item) in enumerate(items):
        if item == value:
            return index
    return None


def find_second_index(value, items):
    iterator = iter(items)
    iterator_1 = iter(items)
    if find_index(value, iterator) is not None:
        if find_index(value, iterator) is not None:
            index = find_index(value, iterator_1) + find_index(value, iterator_1)
            return index + 1


print(find_second_index('1', 'asd1fghj1f'))
