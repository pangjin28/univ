a,b=map(int,input().split())
cnt=0
c=a+b
c=str(c)
for i in c:
    if i== '1':
        cnt+=1
print(cnt)