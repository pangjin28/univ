a = int(input())
f = False
for i in range(2, a):
    if a % i == 0:
        f = True
        break
if f:
    print("C")
else:
    print("P")