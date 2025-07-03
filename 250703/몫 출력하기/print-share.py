count = 0
while count < 3:
    try:
        num = int(input())
        if num % 2 == 0:
            print(num // 2)
            count += 1
    except EOFError:
        break