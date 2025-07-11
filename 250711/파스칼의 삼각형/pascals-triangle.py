a = int(input())
b = [[0]*a for _ in range(a)]

b[0][0] = 1  

for i in range(1, a):  
    b[i][0] = 1  
    for j in range(1, i+1): 
        b[i][j] = b[i-1][j-1] + b[i-1][j]

for i in range(a):
    for j in range(i+1):
        print(b[i][j], end=" ")
    print()
