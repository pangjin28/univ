n=input()
words = input().split()

nums = "".join(words)
for i in range(0,len(nums),5):
    print(nums[i:i+5])