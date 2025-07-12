s = input()
a = s[0]  
b = s[1]  

result = ""

for ch in s:
    if ch == a:
        result += b
    elif ch == b:
        result += a
    else:
        result += ch

print(result)
