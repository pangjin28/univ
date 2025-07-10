a = list(map(int,input().split()))
b = 0
for i in a:
    if i > b:
        b= i
print(b)