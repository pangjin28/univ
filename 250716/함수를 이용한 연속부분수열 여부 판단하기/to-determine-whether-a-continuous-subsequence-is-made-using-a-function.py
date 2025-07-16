def is_subsequence(a, b):
    n1 = len(a)
    n2 = len(b)
    for i in range(n1 - n2 + 1):
        if a[i:i+n2] == b:
            return "Yes"
    return "No"

n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(is_subsequence(a, b))