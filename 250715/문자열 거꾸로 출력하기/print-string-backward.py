while True:
    a= input()
    if a == "END":
        break
    for i in range(len(a)-1,-1,-1):
        print(a[i],end="")
    print()
