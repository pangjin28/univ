N, Q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(Q):
    parts = input().split()

    if parts[0] == "1":
        a = int(parts[1])
        print(arr[a - 1])  # 1-based to 0-based

    elif parts[0] == "2":
        b = int(parts[1])
        found = 0
        for i in range(N):
            if arr[i] == b:
                found = i + 1  # 1-based index
                break
        print(found)

    elif parts[0] == "3":
        s, e = map(int, parts[1:])
        print(' '.join(map(str, arr[s - 1:e])))
