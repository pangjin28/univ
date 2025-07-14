n=input()
m= input()

for i in range(len(m)):
    if m[i] == "L":
       n = n[1:] + n[0]
    elif m[i] == "R":
        n = n[-1] + n[:-1]
print(n)