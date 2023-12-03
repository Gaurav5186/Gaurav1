def integer_partition(n):
    partition = [0] * (n + 1)
    partition[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partition[j] += partition[j - i]
    return partition[n]
n=int(input("Enter a digit"))
print(integer_partition(n))
