N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

max_bomb = -1

for i in range(N):
    for j in range(i+1, N):
        if num[i] == num[j] and j - i <= K:
            if num[i] > max_bomb:
                max_bomb = num[i]
print(max_bomb)
