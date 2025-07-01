a_count = 0

for _ in range(3):
    symptom, temp = input().split()
    temp = float(temp)

    if symptom == 'Y' and temp >= 37:
        a_count += 1

# 결과 판정
if a_count >= 2:
    print('E')
else:
    print('N')