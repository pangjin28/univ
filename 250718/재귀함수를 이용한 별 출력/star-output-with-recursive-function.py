n = int(input())

# Please write your code here.
def sa(n):
    if n ==0:
        return
    sa(n-1)
    print("*" * n)
sa(n)