n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
mi = 100
cnt=0
for i in a:
    if i < mi:
        mi = i
        if i == mi:
            cnt+=1
print(mi, cnt)