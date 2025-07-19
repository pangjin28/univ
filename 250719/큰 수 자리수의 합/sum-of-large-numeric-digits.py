a, b, c = map(int, input().split())

# Please write your code here.
def sa(d):
    if d <10:
        return d
    return sa(d//10) + (d % 10)

d= a*b*c
print(sa(d))