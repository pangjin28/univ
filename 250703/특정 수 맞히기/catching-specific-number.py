while True:
    try:
        a = int(input())
    except EOFError:
        break

    if a < 25:
        print("Higher")
    elif a > 25:
        print("Lower")
    else:
        print("Good")
        break