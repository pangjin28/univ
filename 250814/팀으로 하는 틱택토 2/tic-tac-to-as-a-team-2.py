board = [list(map(int, input().strip())) for _ in range(3)]

lines = []
for r in range(3):
    lines.append([board[r][c] for c in range(3)])
for c in range(3):
    lines.append([board[r][c] for r in range(3)])

lines.append([board[i][i] for i in range(3)])
lines.append([board[i][2 - i] for i in range(3)])

teams = set()

for line in lines:
    unique_nums = set(line)
    if len(unique_nums) == 2:
        teams.add(tuple(sorted(unique_nums)))

print(len(teams))
