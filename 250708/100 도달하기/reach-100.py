a=int(input())
b=[1, a]
i=2
while True:
    b.append(b[i-1] + b[i-2])
    if b[i] > 100:
        break
    i+=1
print(*b)