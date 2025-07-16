a, b = map(int, input().split())

# Please write your code here. 
def sa(a,b):
    cnt=0
    for num in range(a,b+1):
        prime=True
        for i in range(2,num):
            if num % i == 0:
                prime=False
                break
        if not prime:
            continue

        if ((num // 10) + (num % 10)) % 2 == 0:
            cnt+=1
    return cnt
print(sa(a,b))



