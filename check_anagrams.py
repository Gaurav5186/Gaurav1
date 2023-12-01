def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
s=input("Enter a string")
s1=input("Enter a string")
print(are_anagrams(s,s1))
