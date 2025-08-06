n = int(input())
a, b, c = [], [], []

for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(str(num))
    b.append(cnt1)
    c.append(cnt2)

ans = 0

for num in range(123, 988):
    s = str(num)
    
    if '0' in s or len(set(s)) < 3:
        continue

    ok = True

    for i in range(n):
        strike = 0
        ball = 0
        for j in range(3):
            if s[j] == a[i][j]:
                strike += 1
            elif s[j] in a[i]:
                ball += 1

        if strike != b[i] or ball != c[i]:
            ok = False
            break

    if ok:
        ans += 1

print(ans)
