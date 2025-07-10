a= [list(map(int, input().split())) for _ in range(4)]
sum2=0
for i in range(4):
    for j in range(i+1):
        sum2 += a[i][j]
print(sum2)