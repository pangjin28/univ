n = int(input())

# Please write your code here.
def sa(a):
    if a == 0:
        return
    sa(a-1)
    print("HelloWorld")

sa(n)