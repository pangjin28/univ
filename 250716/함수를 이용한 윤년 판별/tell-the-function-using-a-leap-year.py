y = int(input())

# Please write your code here.
def sa(a):
    if a % 4 ==0 and ( a% 100 !=0 or a% 400 ==0):
        return "true"
    else:
        return "false"

print(sa(y))