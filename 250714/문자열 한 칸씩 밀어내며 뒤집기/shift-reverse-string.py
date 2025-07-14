n,m = input().split()
m = int(m)

for i in range(m):
    q = int(input())
    if q == 1:
        n = n[1:] + n[0]
        print(n)
    elif q == 2:
        n = n[-1] + n[:-1]
        print(n)
    else:
        reversed_n = ""
        for j in n:
            reversed_n = j + reversed_n
        n = reversed_n
        print(n)
