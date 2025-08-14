N, M = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = 0

for start in range(N): 
    total = 0
    pos = start
    for _ in range(M):
        total += arr[pos]
        pos = arr[pos] - 1 
    max_sum = max(max_sum, total)

print(max_sum)
