a=int(input())
cnt=0
for i in range(a):
    for j in range(a):
        print(chr(65+cnt),end="")
        cnt+=1
    print()