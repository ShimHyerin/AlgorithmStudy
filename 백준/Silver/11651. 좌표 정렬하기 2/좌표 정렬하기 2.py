n = int(input())

coordinate = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append((x, y))
coordinate.sort()
coordinate = sorted(coordinate, key=lambda x: x[1])
for i in range(n):
    print(coordinate[i][0], coordinate[i][1])