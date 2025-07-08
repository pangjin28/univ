a,b=map(int,input().split())
c= [a, b]
for i in range(2,10):
    c.append(c[i-1]+c[i-2] * 2)
print(*c)