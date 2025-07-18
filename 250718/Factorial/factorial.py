N = int(input())

# Please write your code here.
def sa(a):
    if a == 1:
        return 1
    return a * sa(a-1)

print(sa(N))