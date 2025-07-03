a= int(input())
num= False
for i in range(2,a):
    if a%i == 0:
        num=True
        break
if num:
    print("C")
else:
    print("N")