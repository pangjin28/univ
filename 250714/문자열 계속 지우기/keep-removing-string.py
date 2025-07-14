str_a = input()
str_b = input()

while str_b in str_a:
    str_a = str_a.replace(str_b, "", 1)

print(str_a)
