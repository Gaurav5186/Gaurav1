def is_palindrome(input_str):
    return input_str == input_str[::-1]
s=input("Enter a string")
print(is_palindrome(s))
