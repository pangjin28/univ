a = list(map(int,input().split()))

for i in a:
    if i == 0:
        break
    if i % 2 != 0:
        b = i+3
        print(b,end=" ")
    else:
        c = i // 2
        print(c,end=" ")


