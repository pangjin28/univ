a = list(map(int,input().split()))

for i in range(len(a)-1,-1,-1):
    if a[i] == 0:
        continue
    print(a[i],end=" ")