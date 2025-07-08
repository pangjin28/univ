a= list(map(int,input().split()))
cnt=0
sum=0

if 0 in a:
    idx = a.index(0)
    a =a[:idx]
for i in a:
    if i % 2 ==0:
        cnt+=1
        sum+=i
print(cnt, sum)