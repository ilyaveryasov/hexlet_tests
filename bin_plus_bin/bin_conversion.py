def bin_conversion(number):
    """Decimal to bin conversion function, only for number > 0"""
    result = ''
    while number >= 1:
        if number % 2 > 0:
            result = '1' + result
        else:
            result = '0' + result
        number = number // 2
    return result
