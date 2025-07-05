n = int(input()) 

cnt = 1
for i in range(n):
    if i % 2 == 0:  
        for j in range(n):
            print(cnt, end=' ')
            cnt += 1
    else:  
        temp = []
        for j in range(n):
            temp.append(cnt)
            cnt += 1
        for j in reversed(temp):
            print(j, end=' ')
    print()
