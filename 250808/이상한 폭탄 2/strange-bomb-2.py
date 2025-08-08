N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
maxd= 0
for i in range(N):
    for j in range(i+1, N):
        if num[i] == num[j]:
            if j - i <= K:
                a = num[j]
            maxd = max(maxd, a)

print(maxd)
            