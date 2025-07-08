a = list(map(int, input().split()))

if 0 in a:
    idx = a.index(0)
    a = a[:idx]

for i in range(len(a)-1, -1, -1):
    print(a[i], end=" ")
