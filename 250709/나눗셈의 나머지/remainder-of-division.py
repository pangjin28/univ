A, B = map(int, input().split())
counts = [0] * B

while A > 1:  
    counts[A % B] += 1
    A //= B

print(sum(x ** 2 for x in counts))
