def count_369(A, B):
    count = 0
    for num in range(A, B + 1):
        if any(digit in '369' for digit in str(num)) or num % 3 == 0:
            count += 1
    return count

A, B = map(int, input().split())

print(count_369(A, B))
