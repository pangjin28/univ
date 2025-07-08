a= list(map(int,input().split()))
sum=0
sum2 =0
cnt =0
for i in range(1,len(a),2):
    sum += a[i]
for j in range(2,len(a),3):
    sum2 += a[j]
    cnt+=1
print(f"{sum} {sum2/cnt:.1f}")