a = list(map(int,input().split()))
sum =0

if 0 in a:
    idx= a.index(0)
    a = a[:idx]
for i in a:
    sum+=i
print(f"{sum} {sum/len(a):.1f}")