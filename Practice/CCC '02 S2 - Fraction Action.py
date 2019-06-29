from fractions import Fraction
numerator = int(input())
denominator = int(input())
first = int(numerator/denominator)
if denominator * first != numerator:
    fraction = numerator - denominator*first
    fraction = Fraction(fraction, denominator)
    if first != 0:
        print(str(first) + " " + str(fraction))
    else:
        print(str(fraction))
else:
    print(str(first))
    
