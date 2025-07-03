nums = list(map(int, input().split()))

if all(n % 3 == 0 for n in nums):
    print(1)
else:
    print(0)