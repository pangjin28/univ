cnt = 0
sum_age = 0

while True:
    age = int(input())
    if age < 20 or age > 29:
        break
    sum_age += age
    cnt += 1

average = sum_age / cnt
print(f"{average:.2f}")