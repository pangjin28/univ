A = input()

# Please write your code here.
def sa(A):
    if A == A[::-1]:
        return "Yes"
    else:
        return "No"

print(sa(A))