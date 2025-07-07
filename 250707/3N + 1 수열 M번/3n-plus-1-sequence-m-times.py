a= int(input())
for _ in range(a):
    b = int(input())
    cnt = 0
    while True:
        if b == 1:
            break
        if b % 2 == 0:
            b //= 2
        else:
            b = b * 3 + 1
        cnt += 1
    print(cnt)