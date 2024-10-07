from collections import defaultdict

h: int
w: int
n: int
h, w, n = map(int, input().split())
t: list[str] = list(input())

grid = defaultdict(list)
for i in range(h):
    grid[i] = list(input())

ans: int = 0
for i in range(1, h - 1):
    for j in range(1, w - 1):
        x = i
        y = j
        flag = True
        if grid[x][y] == "#":
            flag = False
        for k in t:
            if k == "L":
                if grid[x][y - 1] == "#":
                    flag = False
                else:
                    y -= 1
            elif k == "R":
                if grid[x][y + 1] == "#":
                    flag = False
                else:
                    y += 1

            elif k == "U":
                if grid[x - 1][y] == "#":
                    flag = False
                else:
                    x -= 1

            elif k == "D":
                if grid[x + 1][y] == "#":
                    flag = False
                else:
                    x += 1
        if flag:
            ans += 1

print(ans)
