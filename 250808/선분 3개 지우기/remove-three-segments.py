n = int(input())
seg = []
for _ in range(n):
    a, b = map(int, input().split())
    seg.append((a, b))

result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            remain = []
            for t in range(n):
                if t != i and t != j and t != k:
                    remain.append(seg[t])

            valid = True
            for x in range(len(remain)):
                for y in range(x+1, len(remain)):
                    a1, b1 = remain[x]
                    a2, b2 = remain[y]
                    if not (b1 < a2 or b2 < a1):
                        valid = False
                        break
                if not valid:
                    break

            if valid:
                result += 1

print(result)
