X, Y = map(int, input().split())

# Please write your code here.
maxd =0
for i in range(X, Y + 1):
    total = 0
    for j in str(i):
        total += int(j)

    maxd=max(maxd, total) 
print(maxd)