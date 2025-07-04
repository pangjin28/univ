n=int(input())
for i in range(1,n+1):
    a = "  " * (n-i)
    b= "* " * (2*i - 1)
    print(a + b)