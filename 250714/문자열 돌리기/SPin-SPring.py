a = input()
print(a)
for _ in range(len(a)):
    a = a[-1]+a[:-1]
    print(a)