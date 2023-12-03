from fractions import Fraction

def square_root_2_expansion(n):
    result = Fraction(1, 2)
    for _ in range(n - 1):
        result = Fraction(1, 2 + result)
    return 1 + result

result = square_root_2_expansion(10)
print(result)
