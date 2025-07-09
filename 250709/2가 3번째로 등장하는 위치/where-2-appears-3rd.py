a = int(input())
b = list(map(int, input().split()))

cnt = 0
for idx in range(a):
    if b[idx] == 2:
        cnt += 1
        if cnt == 3:
            print(idx + 1) 
            break
