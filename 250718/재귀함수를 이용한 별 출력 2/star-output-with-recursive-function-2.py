n = int(input())

# Please write your code here.
def sa(n):
    if n == 0 :
        return
    print("* "*n,end=" ")
    print()
    sa(n-1)
    print("* "*n,end=" ")
    print()
sa(n)