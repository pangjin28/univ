a=int(input())
words = [input() for _ in range(a)] 
b=input()
cnt =0
leng = 0 
for word in words:
    if word[0] ==b:
        cnt+=1
        leng += len(word)

print(f"{cnt} {leng/cnt:.2f}")
