def test_bin(number):
    """Chek a number for binary"""
    string = str(number)
    x = len(string)
    other_numbers = set(['2', '3', '4', '5', '6', '7', '8', '9'])
    counter = 0
    while counter != x:
        if string[counter] in other_numbers:
            return "ERROR: it is not binary number!"
        else:
            counter = counter + 1
    return True
