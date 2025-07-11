a = [[0] * 5 for _ in range(5)]

for i in range(5):
    a[0][i] = 1
    a[i][0] = 1

for j in range(1,5):
    for k in range(1,5):
        a[j][k] = a[j][k-1] + a[j-1][k]

for i in range(5):
    for j in range(5):
        print(a[i][j],end= " ")
    print()