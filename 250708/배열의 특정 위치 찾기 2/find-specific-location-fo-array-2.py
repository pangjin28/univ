a=list(map(int,input().split()))

sum1=0
sum2=0
for i in range(0,len(a),2):
    sum2 += a[i]
for j in range(1,len(a),2):
    sum1 += a[j]

if sum1>sum2:
    print(sum1-sum2)
else:
    print(sum2-sum1)