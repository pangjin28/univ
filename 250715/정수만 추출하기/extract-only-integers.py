a, b = input().split()

idx1 = 0
idx2 = 0

for elem in a:
	if elem <= '9' and elem >= '0':
		idx1 += 1
	else:
		break

for elem in b:
	if elem <= '9' and elem >= '0':
		idx2 += 1
	else:
		break
	
str1 = a[:idx1]
str2 = b[:idx2]
str1 = int(str1)
str2 = int(str2)
print(str1 + str2)
