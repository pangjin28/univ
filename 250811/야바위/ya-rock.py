n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_score = 0

for i in range(1, 4):
    score = 0
    for a, b, c in moves:
        if i == a:
            i = b
        elif i == b:
            i = a

        if i == c:
            score += 1
    max_score = max(max_score, score)

print(max_score)