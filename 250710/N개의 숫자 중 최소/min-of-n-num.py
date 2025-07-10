n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
mi = float('inf')
cnt=0
for i in a:
    if i < mi:
        mi = i
        cnt = 1
    elif i == mi:
        cnt+=1
print(mi, cnt)