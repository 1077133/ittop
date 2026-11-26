words = input().split(",")
a = list(filter(lambda x: len(x.strip()) >= 2 and x.strip()[0].lower() == x.strip()[-1].lower(), words))
print([word.strip() for word in a])
