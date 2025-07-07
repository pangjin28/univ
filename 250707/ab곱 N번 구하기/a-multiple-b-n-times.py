a= int(input())
sum =0
for _ in range(a):
    b,c= map(int,input().split())
    for i in range(b,c+1):
        sum += i 
    print(sum)