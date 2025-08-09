X, Y = map(int, input().split())  
total = 0  

for i in range(X, Y + 1): 
    s = str(i)  
    count = [0] * 10  

    for ch in s:
        count[int(ch)] += 1

    if count.count(1) == 1 and count.count(0) == 8:
        total += 1  

print(total)  
