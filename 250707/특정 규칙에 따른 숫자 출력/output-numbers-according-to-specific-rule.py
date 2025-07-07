a=int(input())
cnt=1
for i in range(a):
    print("  " * i, end="")
    for j in range(a-i):
        print(cnt,end=" ")
        cnt+=1
        if cnt >9:
            cnt = 1
    print()