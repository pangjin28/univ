A, B, C = map(int, input().split())

# Please write your code here.
maxd =0
for i in range(1000):
    for j in range(1000):
        s = A * i + B * j
        if s > C:
            break
        if s <= C:
            maxd= max(maxd, s)

print(maxd)