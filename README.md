// 오름 내림차순 정렬
n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
print(*nums)
nums.sort(reverse=True)
print(*nums)
