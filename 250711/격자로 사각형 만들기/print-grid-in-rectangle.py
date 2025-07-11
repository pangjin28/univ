a = int(input())
b=[[0] * a for _ in range(a)]

for i in range(a):
    b[0][i] = 1
    b[i][0] = 1

for j in range(1, a):
    for k in range(1,a):
        b[j][k] = b[j-1][k]+b[j][k-1]+b[j-1][k-1]

for i in range(a):
    for j in range(a):
        print(b[i][j],end=" ")
    print()