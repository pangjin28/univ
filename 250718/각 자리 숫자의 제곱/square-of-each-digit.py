N = int(input())

# Please write your code here.
def sa(a):
    if a < 10:
        return a**2
    return sa(a//10) + ((a% 10)**2)

print(sa(N))