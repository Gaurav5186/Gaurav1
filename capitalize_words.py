def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())
s=input("Enter a String")
print(capitalize_words(s))
