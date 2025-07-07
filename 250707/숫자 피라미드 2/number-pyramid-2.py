a = int(input())
cnt=1
for i in range(a):
    for j in range(i+1):
        print(cnt,end=" ")
        cnt+=1
    print()