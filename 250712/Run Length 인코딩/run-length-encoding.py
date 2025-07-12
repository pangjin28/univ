A = input().strip()

result = ""
count = 1

for i in range(1, len(A)):
    if A[i] == A[i - 1]:
        count += 1
    else:
        result += A[i - 1] + str(count)
        count = 1

result += A[-1] + str(count)

print(len(result))
print(result)
