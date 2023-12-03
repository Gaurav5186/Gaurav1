def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num
n=int(input("Enter the digit"))
print(is_perfect(n))
