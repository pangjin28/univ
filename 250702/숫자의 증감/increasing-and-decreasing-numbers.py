a, b =input().split()
b = int(b)

if a =="A":
    for i in range(1,b+1):
        print(i,end=" ")
elif a =="D":
    for i in range(b,0,-1):
        print(i, end=" ")