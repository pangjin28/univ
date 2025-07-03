cnt=0
sum =0
while True:

    a=int(input())
    if a >=30:
        break
    sum += a
    cnt += 1
print(f"{sum/cnt:.2f}")
