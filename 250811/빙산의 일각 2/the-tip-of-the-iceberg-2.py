N = int(input())
H = [int(input()) for _ in range(N)]
ans = 0

for t in range(max(H)):
    cnt, prev = 0, False
    for h in H:
        if h > t:
            if not prev: cnt += 1
            prev = True
        else:
            prev = False
    ans = max(ans, cnt)

print(ans)
