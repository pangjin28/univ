a=int(input())
for i in range(a):
    print("  " * i, end="")
    for j in range(a-i,0,-1):
        print(j, end=" ")
    print()