def generate_primitive_pythagorean_triple(limit):
    for m in range(2, int(limit**0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                yield (a, b, c)

result = list(generate_primitive_pythagorean_triple(20))
print(result)
