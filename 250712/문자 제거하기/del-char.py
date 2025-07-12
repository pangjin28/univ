s = input()

while True:
    try:
        idx = int(input())
    except EOFError:
        break  

    if len(s) == 1:
        break
    if idx >= len(s):
        idx = len(s) - 1
    s = s[:idx] + s[idx+1:]
    print(s)
