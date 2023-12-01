def title_case(input_str):
    return ' '.join(word.capitalize() for word in input_str.split())
s=input("Enter a string")
print(title_case(s))
