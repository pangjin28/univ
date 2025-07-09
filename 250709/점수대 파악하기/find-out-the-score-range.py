a = list(map(int, input().split()))
if 0 in a:
    a = a[:a.index(0)]

for i in range(100, 0, -10): 
    cnt = 0
    for score in a:
        if i == 100:
            if score == 100:
                cnt += 1
        else:
            if i <= score < i + 10:
                cnt += 1
    print(f"{i} - {cnt}")
