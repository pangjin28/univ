N = int(input())

# Please write your code here.
def sa(a):
    if a==1:
        return 2
    if a==2:
        return 4
    return (sa(a-1) *sa(a-2)) % 100
    

print(sa(N))