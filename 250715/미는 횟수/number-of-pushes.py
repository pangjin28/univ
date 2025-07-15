A = input()  
B = input()  

for i in range(1, len(A) + 1):
    if A[i:] + A[:i] == B:
        print(i)
        break
else:
    print(-1)
