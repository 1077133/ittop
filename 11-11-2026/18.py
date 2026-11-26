s = input()

for word in s.split():
    if word.lower().startswith("а"):
        print(word)
