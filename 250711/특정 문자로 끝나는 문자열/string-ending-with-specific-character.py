words=[input() for _ in range(10)]
a= input()
found = False
for word in words:
    if word[-1] == a:
        print(word)
        found = True
if not found:
    print("None")