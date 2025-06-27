a = []
for _ in range(3):
    num = list(map(int,input().split()))
    a.append(num)

for i in range(3):
    for j in range(3):
        print(a[i][j] * 3, end=" ")
    print()
