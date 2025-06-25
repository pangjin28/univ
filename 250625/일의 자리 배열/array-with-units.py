a = list(map(int, input().split()))
b= [0] * 10
b[0] = a[0]
b[1] = a[1]
for i in range(2, 10):
    b[i]=(b[i-1]+b[i-2])%10

print(*b)
    
