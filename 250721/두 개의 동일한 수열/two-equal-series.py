n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()
result = "Yes"

for i in range(n):
    if A[i] != B[i]:
        result = "No"
        break
print(result)