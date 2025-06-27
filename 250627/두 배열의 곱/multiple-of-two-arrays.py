a = []
for _ in range(3):
    num = list(map(int, input().split()))
    a.append(num)

input()
b = []
for _ in range(3):
    num2 = list(map(int, input().split()))
    b.append(num2)

for i in range(3):
    for j in range(3):
        print(a[i][j] * b[i][j], end= " ")
    print()