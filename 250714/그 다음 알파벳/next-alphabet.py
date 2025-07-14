a=input()
b=ord(a)
if 'a' <= a <= 'z':
    if b == ord('z'):  
        print('a') 
    else:
        print(chr(b + 1))  