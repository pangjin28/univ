a,b=input().split()
a= int(a)
cnt = 0
for _ in range(a):
    c= input()
    if c == b:
        cnt+=1
print(cnt)