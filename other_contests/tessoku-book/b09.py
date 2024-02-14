n: int
n = int(input())

x: list[list[int]] = [[0] * 1509 for _ in range(1509)]


a: int
b: int
c: int
d: int
for i in range(n):
    a, b, c, d = map(int, input().split())
    x[c][b] += 1
    x[a+1][d+1] += 1
    x[c][d+1] -= 1
    x[a+1][b] -= 1

ans: int = 0
for i in range(1, 1501):
    for j in range(1, 1501):
        if x[i][j] > 0:
            ans += 1

print(ans)