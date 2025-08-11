n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
mind = float("inf")
for i in range(n):
    arr[i] *= 2
    for j in range(n):
        sa =[]
        for k in range(n):
            if k != j:
                sa.append(arr[k])
        sumd = 0

        for l in range(n-2):
            sumd += abs(sa[l+1] - sa[l])
        mind = min(mind, sumd)
    arr[i] //= 2

print(mind)
            