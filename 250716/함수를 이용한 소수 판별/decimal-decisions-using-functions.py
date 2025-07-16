def sum_primes(A, B):
    prime_sum = 0
    for num in range(A, B + 1): 
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):  
            if num % i == 0:
                is_prime = False
                break
        if is_prime: 
            prime_sum += num
    return prime_sum

A, B = map(int, input().split())

print(sum_primes(A, B))
