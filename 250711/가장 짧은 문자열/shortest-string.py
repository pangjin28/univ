a=input()
b=input()
c=input()

if len(a) > len(b) and len(b) > len(c):
    print(len(a)-len(c))
elif len(b) > len(a) and len(a) > len(c):
    print(len(b)-len(c))
else:
    print(len(c)- len(a))