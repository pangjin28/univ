n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def range_sum(arr, start, end):
    return sum(arr[start - 1 : end])  

for a1, a2 in queries:
    print(range_sum(arr, a1, a2))
