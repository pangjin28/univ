N = int(input())

# Please write your code here.
def sa(a):
    if a <= 0:
        return 0
    if a % 2 !=0:
        return a + sa(a-2)
    else:
        return a + sa(a-2)

print(sa(N))