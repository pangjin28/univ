a = input()
b = input()

if len(a) != len(b):
    print("No")
else:
    arr1 = sorted(a)
    arr2 = sorted(b)

    if arr1 == arr2:
        print('Yes')
    else:
        ('No')
