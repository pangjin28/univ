n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def close(x, y):
    return min(abs(x - y), n - abs(x - y)) <= 2

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if (close(i, a1) and close(j, b1) and close(k, c1)) or \
               (close(i, a2) and close(j, b2) and close(k, c2)):
                cnt += 1

print(cnt)
