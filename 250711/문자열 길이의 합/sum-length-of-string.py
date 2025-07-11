n= int(input())
word =[input() for _ in range(n)]
leng=0
for i in range(n):
    leng += len(word[i])
cnt =0
for i in word:
    if i[0] =="a":
        cnt+=1
print(leng, cnt)