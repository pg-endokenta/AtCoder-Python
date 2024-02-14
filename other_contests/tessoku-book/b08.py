n: int
n = int(input())

grid: list[list[int]] = [[0] * 1509 for _ in range(1509)]

x: int
y: int
for i in range(n):
    x, y = map(int, input().split())
    grid[x][y] += 1

z = [[0] * 1509 for _ in range(1509)]

for i in range(1, 1501):
    for j in range(1, 1501):
        z[i][j] = z[i][j-1] + grid[i][j]

for i in range(1, 1501):
    for j in range(1, 1501):
        z[j][i] = z[j-1][i] + z[j][i]

q: int
q = int(input())
for _ in range(q):
    a: int
    b: int
    c: int
    d: int
    a, b, c, d = map(int, input().split())
    print(z[c][d] + z[a-1][b-1] - z[c][b-1] - z[a-1][d])
