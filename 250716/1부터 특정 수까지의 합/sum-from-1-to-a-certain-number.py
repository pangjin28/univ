n = int(input())

# Please write your code here.
def sa(a):
    sum=0
    for i in range(1,a+1):
        sum += i
    return (sum//10)

total = sa(n)
print(total)
