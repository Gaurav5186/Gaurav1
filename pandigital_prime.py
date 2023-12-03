from itertools import permutations
import sympy

def is_pandigital(num_str):
    return all(str(i) in num_str for i in range(1, len(num_str) + 1))

def find_largest_pandigital_prime():
    for i in range(9, 0, -1):
        digits = ''.join(map(str, range(1, i + 1)))
        perms = permutations(digits)
        for perm in sorted(perms, reverse=True):
            num = int(''.join(perm))
            if sympy.isprime(num):
                return num

result = find_largest_pandigital_prime()
print(result)
