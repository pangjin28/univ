a= int(input())
cnt=0
for _ in range(a):
    b=list(map(int,input().split()))
    sum=0
    for i in b:
        sum += i
    if sum // 4 >= 60:
        print("pass")
        cnt+=1
    else:
        print("fail")
print(cnt)