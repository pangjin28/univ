n = int(input())

for i in range(2 * n):
    if i % 2 == 0:  # 홀수 번째 줄 (0-based index) → i=0,2,4,...
        stars = n - (i // 2)
    else:           # 짝수 번째 줄
        stars = (i + 1) // 2
    print('* ' * stars)