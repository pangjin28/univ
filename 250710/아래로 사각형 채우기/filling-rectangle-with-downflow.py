N = int(input())

for i in range(N):
    for j in range(N):
        print((j * N) + (i + 1), end=" ")
    print()
