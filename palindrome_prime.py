def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindromic_prime(start, end):
    for num in range(start, end + 1):
        if is_prime(num) and is_palindrome(num):
            print(num)
        else:
            print("Not a palindrome prime")
            break
n=int(input("Enter a digit"))
s=int(input("Enter a start"))
e=int(input("Enter a end"))
palindromic_prime(s, e)
