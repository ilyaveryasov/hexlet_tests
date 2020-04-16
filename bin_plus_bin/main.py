import bin_conversion
import decimal_conversion
import test_bin
import sys

print('Hello! Before use this program, read readme.md')

number_1 = str(input('enter number 1:'))
if number_1 != '' and test_bin.test_bin(number_1) is True:
    number_2 = str(input('enter number 2:'))
    if number_2 != '' and test_bin.test_bin(number_2) is True:
        a = decimal_conversion.decimal_conversion(number_1)
        b = decimal_conversion.decimal_conversion(number_2)
        print(str(a) + '\n' + str(b))
        result = a + b
        print(str(bin_conversion.bin_conversion(result)))
    else:
        print('ERROR: it is a not bin number')
    sys.exit()
else:
    print('ERROR: it is a not bin number')
    sys.exit()
