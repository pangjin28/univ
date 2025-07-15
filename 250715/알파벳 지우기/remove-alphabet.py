a=input()
b=input()
c=[]
d=[]
for i in range(len(a)):
    if a[i].isdigit():
        c.append(a[i])

for i in range(len(b)):
    if b[i].isdigit():
        d.append(b[i])

e= "".join(c)
f= "".join(d)
print(int(e)+int(f))
