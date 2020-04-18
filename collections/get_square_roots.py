import math


def get_square_roots(number):
    result = []
    if number == 0:
        result.append(math.sqrt(0))
        return result
    elif number < 0:
        return 'ERROR'
    elif number > 0:
        result.append(-1 * math.sqrt(number))
        result.append(math.sqrt(number))
        return result


def get_range(number):
    result = []
    index = 0
    if number <= 0:
        return result
    else:
        result.append(0)
        while index < number - 1:
            result.append(index + 1)
            index = index + 1
        return result
