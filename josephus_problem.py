def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, k) + k) % n

n, k = 7, 3
print(josephus(n, k) + 1)
