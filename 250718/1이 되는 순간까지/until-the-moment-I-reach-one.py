N = int(input())

# Please write your code here.
def sa(a):
    if a == 1:
        return 0
    if a % 2 == 0:
        return 1 + sa(a // 2)
    else:
        return 1 + sa(a // 3)

print(sa(N))