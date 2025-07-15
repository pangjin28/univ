n = int(input())

# Please write your code here.
def saa(a):
    ds=[[0]*a for _ in range(a)]
    cnt = 1
    for i in range(a):
        for j in range(a):
            ds[i][j] = cnt
            cnt+=1
            if cnt > 9:
                cnt = 1

    for i in range(a):
        for j in range(a):
            print(ds[i][j],end=" ")
        print()
saa(n)
