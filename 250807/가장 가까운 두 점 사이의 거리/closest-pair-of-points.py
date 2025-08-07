n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def sq(p1, p2):
    return (p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2

mind = float("inf")
for i in range(n):
    for j in range(i+1,n):
        mind = min(mind, sq(points[i],points[j]))

print(mind)
