a,b = map(int, input().split())
c = 1
for i in range(a,b+1):
    c *= i
print(c)