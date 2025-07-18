n = int(input())

# Please write your code here.
def sa(a):
    if a ==0:
        return
    sa(a-1)
    print(a,end=" ")

def sad(a):
    if a ==0:
        return
    print(a,end=" ")
    sad(a-1)

sa(n)
print()
sad(n)