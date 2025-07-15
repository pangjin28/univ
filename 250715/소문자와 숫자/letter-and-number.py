a= input()
b=[]
for i in range(len(a)):
    if a[i].isalpha():
        b.append(a[i].lower())
    elif a[i].isdigit():
        b.append(a[i])
print("".join(b))