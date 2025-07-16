n = int(input())

# Please write your code here.
def sa(n):
    if n %2==0 and ((n // 10) + (n % 10)) % 5 ==0:
        return "Yes"
    else:
        return "No"

print(sa(n))