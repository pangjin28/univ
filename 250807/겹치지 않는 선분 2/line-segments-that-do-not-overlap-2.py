n = int(input())
lines = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    lines.append((x1, x2))

count = 0

for i in range(n):
    x1, x2 = lines[i]
    intersect = False
    for j in range(n):
        if i == j:
            continue
        y1, y2 = lines[j]
        if (x1 < y1 and x2 > y2) or (x1 > y1 and x2 < y2):
            intersect = True
            break
    if not intersect:
        count += 1

print(count)
