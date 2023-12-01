from collections import Counter
def word_frequency(s):
    words = s.split()
    return Counter(words)
s=input("Enter a string")
print(word_frequency(s))
