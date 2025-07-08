a, b = map(int, input().split())
c = [a, b]

while len(c) < 10:
    next_val = (c[-1] + c[-2]) % 10  
    c.append(next_val)

print(*c)
