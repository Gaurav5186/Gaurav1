def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num*num, limit + 1, num):
                is_prime[multiple] = False
    for num in range(max(2, int(limit**0.5) + 1), limit + 1):
        if is_prime[num]:
            primes.append(num)
    print(primes)

sieve_of_eratosthenes(50)
