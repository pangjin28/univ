a=input()
n=int(input())

for i in range(len(a)-1, len(a) - n-1,-1):
    print(a[i],end="")