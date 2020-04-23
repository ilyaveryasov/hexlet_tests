def rotate(l):
    print(l)
    length_list = len(l) - 1
    list_length = len(l)
    index = 0
    l.insert(index, l[length_list])
    l.pop(list_length)
    return l


list1 = [1, 2, 3, 4, 5]
print(rotate(list1))
