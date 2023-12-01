def is_rotation(str1, str2):
    return len(str1) == len(str2) and str2 in str1 + str1
s=input("Enter a string")
s1=input("Enter a string")
print(is_rotation(s,s1))
