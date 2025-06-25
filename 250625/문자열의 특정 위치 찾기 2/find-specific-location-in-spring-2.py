words = ["apple", "banana", "grape", "blueberry", "orange"]

a = input()
b=[]

for i in words:
    if i[2] == a or i[3] == a:
        b.append(i)
    
for j in b:
    print(j)

print(len(b))