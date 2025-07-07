for i in range(1, 20):  
    for j in range(1, 18, 2):  
        left = f"{i} * {j} = {i * j}"
        right = f"{i} * {j+1} = {i * (j+1)}"
        print(left, '/', right)
    print(f"{i} * 19 = {i * 19}")