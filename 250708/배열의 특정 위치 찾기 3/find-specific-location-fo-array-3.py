a=list(map(int,input().split()))

if 0 in a:
    idx = a.index(0)
    a =a[idx-3:idx]
sum=0
for i in a:
    sum +=i
print(sum)