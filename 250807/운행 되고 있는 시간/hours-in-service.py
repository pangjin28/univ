n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

max_time = 0

for i in range(n):
    time_line = [0] * 1001  
    for j in range(n):
        if i == j:
            continue  
        a, b = times[j]
        for t in range(a, b):
            time_line[t] = 1 

    total = sum(time_line)  
    max_time = max(max_time, total)

print(max_time)
