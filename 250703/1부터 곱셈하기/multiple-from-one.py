a=int(input())
b = 1
for i in range(1,11):
    b *= i 
    if b >= a:
        print(i)
        break