a= input().split()

if len(a[0]) > len(a[1]):
    print(a[0], len(a[0]))
elif len(a[0]) < len(a[1]):
    print(a[1], len(a[1]))
else:
    print("same")