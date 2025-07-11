n=int(input())
num =1
a = [[0] * n for _ in range(n)]
for j in range(n-1,-1,-1):
    if j % 2 ==0:
        for i in range(n):
            a[i][j] = num
            num +=1
    else:
        for i in range(n-1,-1,-1):
            a[i][j] = num
            num+=1

for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()