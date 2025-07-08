a = int(input())
cnt = 0
i = 1
result = []

while True:
    num = a * i
    result.append(num)

    if num % 5 == 0:
        cnt += 1
        if cnt == 2:
            break
    i += 1

print(*result)
