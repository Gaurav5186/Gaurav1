def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    result = n * factorial(n - 1)
    memo[n] = result
    return result

result = factorial(10)
print(result)
