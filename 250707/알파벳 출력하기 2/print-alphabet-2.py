a=int(input())
cnt = 0
for i in range(a):
    print("  " * i,end="")
    for j in range(a-i):
        print(chr(65+cnt%26),end=" ")
        cnt+=1
    print()
