n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def find_lcm(numbers, index=0):
    if index == len(numbers) - 1:
        return numbers[index]
    return lcm(numbers[index], find_lcm(numbers, index + 1))

print(find_lcm(numbers))

