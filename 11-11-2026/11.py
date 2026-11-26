s = input()
words = s.split()

if words:
    print(max(words, key=len))
