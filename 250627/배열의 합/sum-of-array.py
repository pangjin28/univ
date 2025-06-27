a = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    b = 0
    for j in range(4):
        b += a[i][j]
    print(b)
