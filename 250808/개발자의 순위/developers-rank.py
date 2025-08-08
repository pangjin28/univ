k, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.
count = 0 

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            continue
        valid = True
        for race in arr:
            if race.index(a) > race.index(b):  
                valid = False
                break
        if valid:
            count += 1

print(count)
