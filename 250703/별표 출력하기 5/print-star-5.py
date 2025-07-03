N = int(input())

for i in range(N):  # i = 0, 1, 2, ...
    for j in range(N - i):
        print("*" * (N - i), end=" ")
    print()