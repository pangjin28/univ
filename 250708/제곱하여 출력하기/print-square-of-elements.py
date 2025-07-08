a= int(input())
b= list(map(int,input().split()))

c = [ d**2 for d in b]
for i in c:
    print(i,end=" ")