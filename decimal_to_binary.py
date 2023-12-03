def decimal_to_binary(num):
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    print(binary)
n=int(input("Enter the digit"))
decimal_to_binary(n)
