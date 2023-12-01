def count_vowels(input_str):
    return sum(1 for char in input_str if char.lower() in 'aeiou')
s=input("Enter a string")
print(count_vowels(s))
