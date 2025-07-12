a=input()
b = a[1]
c = a[0]

for i in a:
    if i == b:
        print(c,end="")
    else:
        print(i,end="")