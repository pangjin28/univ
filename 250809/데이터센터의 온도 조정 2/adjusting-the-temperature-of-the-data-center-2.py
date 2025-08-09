N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
maxd =0
for temp in range(-100, 101):
    total = 0
    for ta, tb in ranges:
        if temp < ta:
            total += C
        elif ta <= temp <= tb:
            total += G
        else:
            total += H
    maxd = max(maxd, total)

print(maxd)
 