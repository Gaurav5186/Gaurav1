import sympy

def find_prime_constellation(start, length):
    primes = []
    current = start
    while len(primes) < length:
        if sympy.isprime(current):
            primes.append(current)
        current += 1
    return primes

result = find_prime_constellation(10**6, 5)
print(result)
