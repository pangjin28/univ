cnt=0
b=[]
while True:
    a= input()
    if a == "0":
        break
    cnt+=1
    if cnt % 2 != 0:
        b.append(a)

print(cnt)
for i in range(len(b)):
    print(b[i])