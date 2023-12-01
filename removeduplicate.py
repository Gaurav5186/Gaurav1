def remove_duplicates(input_str):
    return ''.join(sorted(set(input_str), key=input_str.index))
s=input("Enter a string")
print(remove_duplicates(s))
