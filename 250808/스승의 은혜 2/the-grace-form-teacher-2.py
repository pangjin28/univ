N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

maxd = 0

for i in range(N):
    discounted = list(P)
    discounted[i] //= 2
    discounted.sort()

    cnt = 0
    total = 0
    for price in discounted:
        if total + price > B:
            break
        total += price
        cnt += 1

    maxd = max(maxd, cnt)

print(maxd)
