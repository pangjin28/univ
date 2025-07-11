n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]

num = 1

for k in range(n + m - 1):
    for i in range(k + 1):
        x = i
        y = k - i
        if 0 <= x < n and 0 <= y < m:
            board[x][y] = num
            num += 1


for row in board:
    print(' '.join(map(str, row)))
