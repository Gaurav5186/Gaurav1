from sympy import I, factorint

def prime_factorization_gaussian_integers(z):
    factorization = factorint(z)
    result = []
    for prime, exponent in factorization.items():
        result.extend([prime] * exponent)
    return result

result = prime_factorization_gaussian_integers(7 + 4*I)
print(result)
