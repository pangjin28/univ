N = int(input())

# Please write your code here.
def sa(a):
    if a == 0:
        return
    print(a,end=" ")
    sa(a-1)
    print(a,end=" ")
sa(N)