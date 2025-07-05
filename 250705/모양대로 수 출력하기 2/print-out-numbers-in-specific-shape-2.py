N = int(input())

for i in range(N):            # i: 행 인덱스
    for j in range(N):        # j: 열 인덱스
        # 2, 4, 6, 8 → 인덱스 0~3 순환 → ((i+j) % 4) → 값으로 바꾸려면 *2 + 2
        value = ((i + j) % 4) * 2 + 2
        print(value, end=' ')
    print()
