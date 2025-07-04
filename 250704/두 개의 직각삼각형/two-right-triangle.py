n = int(input())

for i in range(n):
    left = '*' * (n - i)          # 왼쪽 삼각형
    middle = ' ' * (2 * i)        # 중간 공백
    right = '*' * (n - i)         # 오른쪽 삼각형
    print(left + middle + right)
