A, B, C = map(int, input().split())

# Please write your code here.
maxd =0
for i in range(C // A + 1):
    for j in range(C // B + 1):
        s = A * i + B * j
        if s <= C:
            maxd= max(maxd, s)

print(maxd)