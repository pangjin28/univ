text = input()
pattern = input()

# Please write your code here.
def sa():
    a= len(text)
    b= len(pattern)

    for i in range(a-b+1):
        if text[i:i+b] == pattern:
            return i
    else:
        return -1

print(sa())