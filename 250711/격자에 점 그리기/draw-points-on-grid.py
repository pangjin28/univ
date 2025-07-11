n, m = map(int, input().split())
c = [[0]*n for _ in range(n)]
num =1
for _ in range(m):
    a, b = map(int, input().split())
    c[a-1][b-1] = num
    num +=1
for i in range(n):
    for j in range(n):
        print(c[i][j], end=' ')
    print()