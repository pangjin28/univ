n= int(input())
sum =0
for _ in range(n):
    a= int(input())
    sum += a
b = str(sum)
print(b[1:]+b[0])