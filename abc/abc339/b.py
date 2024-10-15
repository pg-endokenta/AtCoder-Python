h: int
w: int
n: int

h, w, n = map(int, input().split())

grid = [["."] * w for _ in range(h)]


class Agent:
    def __init__(self, x, y, direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction

    # direction: 0: up, 1: right, 2: down, 3: left

    def move(self):
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        self.x += dx[self.direction]
        self.y += dy[self.direction]

        if self.x < 0:
            self.x += w
        elif self.x >= w:
            self.x -= w
        if self.y < 0:
            self.y += h
        elif self.y >= h:
            self.y -= h

    def rotate(self, direction):
        self.direction = (self.direction + direction) % 4


agent = Agent(0, 0, 0)

for i in range(n):
    if grid[agent.y][agent.x] == ".":
        grid[agent.y][agent.x] = "#"
        agent.rotate(1)
        agent.move()

    else:
        grid[agent.y][agent.x] = "."
        agent.rotate(-1)
        agent.move()


for row in grid:
    print("".join(row))
