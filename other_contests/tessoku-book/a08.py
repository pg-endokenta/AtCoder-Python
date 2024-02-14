h: int
w: int
h, w = map(int, input().split())
x: list[list[int]] = [[0] * (w+1) for _ in range(h+1)]


input_row: list[int]
for i in range(1,h+1):
    input_row = list(map(int, input().split()))
    x[i][0] = [0]
    for j in range(w):
        x[i][j+1] = input_row[j]

z: list[list[int]] = [[0] * (w+1) for _ in range(h+1)]

for i in range(h+1):
    for j in range(1,w+1):
        z[i][j] = z[i][j-1] + x[i][j]

for i in range(w+1):
    for j in range(1,h+1):
        z[j][i] = z[j-1][i] + z[j][i]

q: int
q = int(input())

a: int
b: int
c: int
d: int
for _ in range(q):
    a, b, c, d = map(int, input().split())
    print(z[c][d] + z[a-1][b-1] - z[c][b-1] - z[a-1][d])
