
n = int(input()) 
nums = list(map(int, input().split()))  


max_num = -1

for i in range(n):
    count = 0 
    for j in range(n):
        if nums[i] == nums[j]:
            count += 1
    if count == 1:
        max_num = max(max_num, nums[i])

print(max_num)
