a= list(map(int,input().split()))
b=[]
for i in range(5):
    b.append(chr(a[i]))
print(*b)