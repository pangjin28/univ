a= int(input())
b= list(map(float,input().split()))
sum=0
for i in range(a):
    sum += b[i]
c = sum/a
print(f"{c:.1f}")
if c >= 4.0:
    print("Perfect")
elif c>=3.0:
    print("Good")
else:
    print("Poor")