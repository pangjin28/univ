a= int(input())
sum =1
for _ in range(a):
    b,c= map(int,input().split())
    for i in range(b,c+1):
        sum *= i 
    print(sum)
    sum = 1