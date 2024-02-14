n: int
n = int(input())

x: list[list[int]] = [[0] * 1509 for _ in range(1509)]


a: int
b: int
c: int
d: int
for i in range(n):
    a, b, c, d = map(int, input().split())
    x[a][b] += 1
    x[c][d] += 1
    x[a][d] -= 1
    x[c][b] -= 1

z: list[list[int]] = [[0] * 1509 for _ in range(1509)]

for i in range(1, 1501):
    for j in range(1, 1501):
        z[i][j] = z[i][j-1] + x[i][j]

for i in range(1, 1501):
    for j in range(1, 1501):
        z[j][i] = z[j-1][i] + z[j][i]

ans: int = 0
for i in range(1, 1501):
    for j in range(1, 1501):
        if z[i][j] > 0:
            ans += 1

print(ans)

