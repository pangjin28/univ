A = input()
B = input()

for i in range(len(A)):  
    if A[i:] + A[:i] == B:
        print(i)
        break
else:
    print(-1)
