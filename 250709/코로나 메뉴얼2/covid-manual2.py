r =[0] * 4
for _ in range(3):
    a,b = input().split()
    b= int(b)

    if a == "Y" and b >=37:
        r[0] += 1
    elif a == "N" and b >=37:
        r[1] += 1
    elif a=="Y" and b < 37:
        r[2] += 1
    else:
        r[3] += 1

output = f"{r[0]} {r[1]} {r[2]} {r[3]}"
if r[0] >= 2:
    output += " E"  # 위험상황이면 E 추가

print(output)
