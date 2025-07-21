n = int(input())

# Please write your code here.
def sa(a, cnt =0):
    if a == 1:
        return cnt
    if a % 2 == 0:
        return sa(a //2, cnt + 1)
    else:
        return sa(a*3 +1, cnt+1)
    
print(sa(n))