h: int
w: int
n: int
h, w, n = map(int, input().split())

grid = [[0] * 1509 for _ in range(1509)]

a: int
b: int
c: int
d: int
for i in range(n):
    a, b, c, d = map(int, input().split())
    grid[a][b] += 1
    grid[c + 1][d + 1] += 1
    grid[a][d + 1] -= 1
    grid[c + 1][b] -= 1

z: list[list[int]] = [[0] * 1509 for _ in range(1509)]

for i in range(1, 1501):
    for j in range(1, 1501):
        z[i][j] = z[i][j - 1] + grid[i][j]

for i in range(1, 1501):
    for j in range(1, 1501):
        z[j][i] = z[j - 1][i] + z[j][i]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(z[i][j], end=" ")
    print()
