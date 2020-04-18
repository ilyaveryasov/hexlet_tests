def duplicate(l):
    len_list = len(l)
    index = 0
    print('lenght_list: ' + str(len_list))
    while index != len_list:
        l.append(l[index])
        index = index + 1
        print('iteration: -->' + str(index) + ' list: -->' + str(l))
    return l
