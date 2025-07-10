a = []
for _ in range(4):
    a.append(list(map(int, input().split())))
    
sum2=0
for i in range(4):
    for j in range(i+1):
        sum2 += a[i][j]
print(sum2)