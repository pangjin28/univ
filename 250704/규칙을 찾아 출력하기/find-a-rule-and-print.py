n = int(input())

for i in range(n):
    if i == 0 or i == n - 1:
        print('* ' * n)
    else:
        line = ''
        for j in range(n):
            if j < i:
                line += '* '
            elif j == n - 1:
                line += '*'
            else:
                line += '  '
        print(line)
