N = int(input())

# Please write your code here.
def sa(a):
    if a == 1:
        return 1
    if a == 2:
        return 1
    return sa(a-1) + sa(a-2)
print(sa(N))