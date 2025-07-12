a=input()
n=int(input())

if n > len(a):
    for i in range(len(a)-1, -1,-1):
        print(a[i],end="")
else:
    for i in range(len(a)-1, len(a) - n-1,-1):
        print(a[i],end="")
