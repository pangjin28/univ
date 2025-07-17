n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def sa(n,arr):
    for i in range(n):
        print(abs(arr[i]), end=" ")

sa(n,arr)