X, Y = map(int, input().split())

# Please write your code here.

total = 0
for i in range(X, Y + 1):
    s = str(i)
    if len(set(s)) == 2:
        total+=1
print(total)
