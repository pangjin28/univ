n = int(input())

# 첫 줄
print('* ' * n)

# 중간 위쪽 (1부터 n-1까지 증가)
print('*')
for i in range(n - 1, 1, -1):
    print('* ' * i)
for i in range(2, n):
    print('* ' * i)
print('*')

# 마지막 줄
print('* ' * n)
