def is_armstrong(num):
    order = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum
num=int(input("Enter the digit"))
print(is_armstrong(num))
