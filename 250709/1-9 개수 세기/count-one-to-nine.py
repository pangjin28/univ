a=int(input())
b= list(map(int,input().split()))
for i in range(1, 10):
    cnt = 0
    for c in b:
        if c == i:
            cnt+=1
    print(cnt)