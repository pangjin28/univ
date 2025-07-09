A, B = map(int, input().split())

counts = [0] * B  

while A >= 1:
    remainder = A % B
    counts[remainder] += 1
    A //= B

result = sum(x ** 2 for x in counts)
print(result)
