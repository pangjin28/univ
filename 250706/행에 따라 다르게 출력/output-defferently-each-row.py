n=int(input())
for i in range(n):
    for j in range(n):
        if i%2==0:
            print(j+1+3*i*n//2, end=' ')
        else:
            print(n*((i+(i+1)//2)-1)+(2*j+2), end=' ')
    print()
