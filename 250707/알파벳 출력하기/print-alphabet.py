a=int(input())
cnt = 0
for i in range(a):
    for j in range(i+1):
        print(chr(65+cnt%26),end="")
        cnt+=1
    print()