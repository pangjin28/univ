
numbers = list(map(int, input().split()))

# 초기값 설정
max_below_500 = -1  
min_above_500 = 1001  

for num in numbers:
    if num < 500:
        max_below_500 = max(max_below_500, num)
    elif num > 500:
        min_above_500 = min(min_above_500, num)

# 결과 출력
print(max_below_500, min_above_500)
