import sympy

def is_carmichael_number(n):
    if not sympy.isprime(n):
        for a in range(2, n):
            if pow(a, n - 1, n) != 1:
                return False
        return True
    return False

result = [i for i in range(2, 101) if is_carmichael_number(i)]
print(result)
