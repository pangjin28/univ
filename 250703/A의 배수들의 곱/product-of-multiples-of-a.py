a,b = map(int, input().split())
c=1
for i in range(1,b+1):
    if i % a == 0:
        c*=i
print(c)