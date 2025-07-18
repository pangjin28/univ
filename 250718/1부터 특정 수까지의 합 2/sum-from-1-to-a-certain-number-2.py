N = int(input())

# Please write your code here.
def sa(a):
    if a == 0:
        return 0
    return a + sa(a-1)
    

print(sa(N))