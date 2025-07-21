N = int(input())

# Please write your code here.
def sa(a):
    if a ==1:
        return 1
    if a== 2:
        return 2
    return (sa(a//3) +sa(a-1))

print(sa(N))