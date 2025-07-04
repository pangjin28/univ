n = int(input())

for i in range(n):
    spaces = '  ' * i  # 공백 2칸 (별+공백 폭 맞추기)
    stars = '* ' * (2 * (n - i) - 1)
    print(spaces + stars)