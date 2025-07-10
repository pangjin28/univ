a= list(map(int,input().split()))
mi=a[0]
ma=a[0]
for i in a:
    if i == 999 or i== -999:
        break
    if i < mi:
        mi = i
    if i > ma:
        ma = i
print(ma,mi)