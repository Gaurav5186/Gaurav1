def find_longest_word(sentence):
    return max(sentence.split(), key=len)
s=input("Enter a string")
print(find_longest_word(s))
