n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
best_pos = 0
max_score = 0

for start in range(1, 4):
    pos = start
    score = 0
    for a, b, c in moves:
        if pos == a:
            pos = b
        elif pos == b:
            pos = a

        if pos == c:
            score += 1
    if score >= max_score:
        max_score = score
        best_pos = start

print(best_pos)