a=int(input())
for i in range(a):
    if i % 2 == 0:
        for j in range(a):
            print(j+1, end="")
    else:
        for j in range(a):
            print(a-j, end="")
    print()