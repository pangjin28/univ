n = int(input())

# 상단 (1 ~ N)
for i in range(1, n + 1):
    stars = '* ' * i       # 별과 공백 반복
    print(' ' * (n - i) + stars)

# 하단 (N+1 ~ 2N-1)
for i in range(n - 1, 0, -1):
    stars = '* ' * i
    print(' ' * (n - i) + stars)
