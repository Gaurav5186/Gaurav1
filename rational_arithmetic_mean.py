from fractions import Fraction

def rational_arithmetic_mean(a, b):
    return (Fraction(a) + Fraction(b)) / 2

result = rational_arithmetic_mean(3, 5)
print(result)
