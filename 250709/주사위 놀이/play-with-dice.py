a=list(map(int,input().split()))
for i in range(1,7):
    cnt = 0
    for b in a:
        if b == i:
            cnt+=1
    print(f"{i} - {cnt}")