def check_alphabets(A):
    if len(set(A)) >= 2:
        print("Yes")
    else:
        print("No")

A = input()
check_alphabets(A)
