n = int(input())
a = [[0]*n for _ in range(n)]

num = 1

for j in range(n-1, -1, -1):  
    if (n - 1 - j) % 2 == 0:  
        for i in range(n-1, -1, -1):
            a[i][j] = num
            num += 1
    else:  
        for i in range(n):
            a[i][j] = num
            num += 1

for row in a:
    print(*row)
