a=input()
ex=False
am =False
for i in range(len(a)-1):
    if a[i] == "e" and a[i+1]=="e":
        ex=True
    if a[i] == "a" and a[i+1]=="b":
        am=True

if ex:
    print("Yes",end=" ")
else: print("No",end=" ")

if am:
    print("Yes")
else: print("No")