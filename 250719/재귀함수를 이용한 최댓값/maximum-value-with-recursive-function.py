n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def sa(arr):
    m = 0
    for i in range(len(arr)):
        m= max(m, arr[i])
    return m

print(sa(arr))