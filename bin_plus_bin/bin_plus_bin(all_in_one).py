def decimal_conversion_add(number1, number2):
    string1 = str(number1)
    string2 = str(number2)
    x1 = len(string1)
    x2 = len(string2)
    result1 = 0
    result2 = 0
    first_count1 = 0
    first_count2 = 0
    counter1 = 0
    counter2 = 0
    while counter1 < x1:
        if string1[counter1] == '1':
            result1 = first_count1 * 2 + 1
        else:
            result1 = first_count1 * 2 + 0
        first_count1 = result1
        counter1 = counter1 + 1
    while counter2 < x2:
        if string2[counter2] == '1':
            result2 = first_count2 * 2 + 1
        else:
            result2 = first_count2 * 2 + 0
        first_count2 = result2
        counter2 = counter2 + 1
    result3 = result1 + result2
    result4 = ''
    while result3 >= 1:
        if result3 % 2 > 0:
            result4 = '1' + result4
        else:
            result4 = '0' + result4
        result3 = result3 // 2
    return result4


print(decimal_conversion_add('1001', '1001'))
