a = input() 
b = []  

for i in range(len(a)):
    if a[i].isalpha():
        b.append(a[i].upper())

print("".join(b))
