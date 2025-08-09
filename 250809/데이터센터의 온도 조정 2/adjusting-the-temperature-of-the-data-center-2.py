N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
min_temp = min(ta for ta, tb in ranges) -1
max_temp = max(tb for ta, tb in ranges) +1

maxd = 0

for temp in range(min_temp, max_temp + 1):

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
 