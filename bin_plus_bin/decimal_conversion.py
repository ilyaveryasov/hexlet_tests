def decimal_conversion(number):
    """ Conversion to decimal system"""
    string = str(number)
    x = len(string)  # Calculate the length of the string
    result = 0
    first_count = 0
    counter = 0
    while counter < x:
        if string[counter] == '1':
            result = first_count * 2 + 1
        else:
            result = first_count * 2 + 0
        first_count = result
        counter = counter + 1
    return result
