n= int(input())
word =[input() for _ in range(n)]

leng = len(word[0]) + len(word[1]) + len(word[2])

cnt =0
for i in word:
    if i[0] =="a":
        cnt+=1
print(leng, cnt)