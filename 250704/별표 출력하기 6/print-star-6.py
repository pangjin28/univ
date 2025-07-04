n = int(input())

# 윗부분
for i in range(n):
    spaces = '  ' * i
    stars = '* ' * ((2 * n - 1) - 2 * i)
    print(spaces + stars)

# 아랫부분
for i in range(n - 2, -1, -1):
    spaces = '  ' * i
    stars = '* ' * ((2 * n - 1) - 2 * i)
    print(spaces + stars)