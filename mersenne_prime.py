import sympy

def find_mersenne_prime(exponent):
    mersenne_number = 2**exponent - 1
    if sympy.isprime(mersenne_number):
        return mersenne_number
    else:
        return None

result = find_mersenne_prime(17)
print(result)
