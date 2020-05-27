def hamming_weight(number):
    bin_string = str(bin(number))
    count = 0
    for i in bin_string:
        if i == '1':
            count = count + 1
    return count


print(hamming_weight(100))