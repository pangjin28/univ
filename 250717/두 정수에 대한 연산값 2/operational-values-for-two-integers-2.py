a, b = map(int, input().split())

# Please write your code here.
def sa(n,m):
    if n>m:
        m += 10
        n *= 2
    else:
        n += 10
        m *= 2
    return n,m

c,d=sa(a,b)
print(c,d)