N = int(input())  
points = [tuple(map(int, input().split())) for _ in range(N)]

def get_rect_area(points):
    min_x = min(points, key=lambda p: p[0])[0]
    max_x = max(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    return (max_x - min_x) * (max_y - min_y)

min_area = float('inf')

for i in range(N):
    new_points = points[:i] + points[i+1:]
    min_area = min(min_area, get_rect_area(new_points))

print(min_area)
