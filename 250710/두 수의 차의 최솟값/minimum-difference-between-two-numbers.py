
N = int(input()) 
nums = list(map(int, input().split()))  


min_diff = float('inf')


for i in range(N):
    for j in range(i + 1, N):
        diff = abs(nums[i] - nums[j])
        min_diff = min(min_diff, diff)


print(min_diff)
