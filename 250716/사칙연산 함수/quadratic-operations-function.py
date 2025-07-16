a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def plus(a,c):
    return a+c

def minus(a,c):
    return a-c

def mul(a,c):
    return a*c 

def div(a,c):
    return int(a/c)

if o == "+":
    re = plus(a,c) 
    print(f"{a} {o} {c} = {re}")  
elif o == "-":
    re = minus(a,c) 
    print(f"{a} {o} {c} = {re}")
elif o == "*":
    re = mul(a,c) 
    print(f"{a} {o} {c} = {re}")
elif o == "/":
    re = div(a,c) 
    print(f"{a} {o} {c} = {re}")
else:
    print("False")