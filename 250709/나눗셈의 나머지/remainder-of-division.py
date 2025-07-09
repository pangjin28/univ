A, B = map(int, input().split())
counts = [0] * B

while A > 1:  
    A, r = divmod(A, B)
    counts[r] += 1

print(sum(x ** 2 for x in counts))
