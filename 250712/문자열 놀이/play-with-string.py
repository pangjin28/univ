string, q = input().split()
q = int(q)
leng = len(string)

for _ in range(q):
	quest = input().split()

	if int(quest[0]) == 1:
		a = int(quest[1])
		b = int(quest[2])
		
		tmp = string[a - 1]
		string = string[:a - 1] + string[b - 1] + string[a:]
		
		string = string[:b - 1] + tmp + string[b:]
		print(string)
	
	else:
		a = quest[1]
		b = quest[2]
	
		for i in range(leng):
			if string[i] == a:
				string = string[:i] + b + string[i + 1:]

		print(string)
