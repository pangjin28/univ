a= list(map(int,input().split()))
if 0 in a:
    idx = a.index(0)
    a=a[:idx]

for i in range(1,10):
    cnt = 0
    for b in a:
        if b // 10 == i:
            cnt+=1
    print(f"{i} - {cnt}")