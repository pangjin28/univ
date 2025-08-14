N = int(input())
str = input()

# Please write your code here.
for i in range(1,N+1):
    seen = set()
    sad = False

    for j in range(N - i +1):
        sub = str[j : j + i]
        if sub in seen:
            sad = True
            break
        seen.add(sub)

    if not sad:
        print(i)
        break
