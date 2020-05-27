def lenght_of_last_word(string):
    last_index = len(string) - 1
    print('last_index_start= ' + str(last_index))
    print('last_element= ' + string[last_index])
    new_string = ''
    if string == '':
        return 0
    elif string[last_index] == ' ' or string[last_index] == '\n' or string[last_index] == '\t':
        print('string= ' + str(string))
        for (i, e) in enumerate(string[::-1]):
            print(e)
            print('Start FOR!!!')
            if e == ' ' or e == '\n' or e == '\t':
                last_index = last_index - 1
                print('last_index= ' + str(last_index))
                if last_index < 0:
                    return 0
            else:
                break
        new_string = string[0:last_index + 1]
        new_string = new_string[::-1]
    else:
        new_string = string[::-1]
    for i, e in enumerate(new_string):
        if e == ' ':
            break
        if i == 0 or i == 1:
            i = i + 1
    return [new_string, len(new_string[:i])]


print(lenght_of_last_word('hi'))
