N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

maxd = 0


for i in range(N):
    prices = []
    for idx in range(N):
        p, s = gifts[idx]
        if idx == i: 
            p //= 2
        prices.append((p, s))

    prices.sort(key=lambda x: x[0] + x[1])

    total = 0
    cnt = 0
    for p, s in prices:
        if total + p + s > B:
            break
        total += p + s
        cnt += 1

    maxd = max(maxd, cnt)

print(maxd)
