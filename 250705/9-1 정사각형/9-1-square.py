a= int(input())
cnt = 9
for _ in range(a):
    for _ in range(a):
        print(cnt, end="")
        cnt -= 1
        if cnt < 1:
            cnt = 9
    print()