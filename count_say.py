def count_and_say(n):
    if n == 1:
        return '1'
    prev = count_and_say(n - 1)
    result = ''
    count = 1
    for i in range(1, len(prev)):
        if prev[i] == prev[i - 1]:
            count += 1
        else:
            result += str(count) + prev[i - 1]
            count = 1
    result += str(count) + prev[-1]
    return result
n=int(input("Enter the digit"))
print(count_and_say(n))
