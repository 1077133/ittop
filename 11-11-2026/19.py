import string

s = input().lower()

for c in string.punctuation:
    s = s.replace(c, "")

words = s.split()

if words:
    most_common = max(set(words), key=words.count)
    print(most_common)
