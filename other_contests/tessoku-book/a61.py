n: int
m: int
n, m = map(int, input().split())

graph: list[list[int]] = [[] for _ in range(n + 1)]

a: int
b: int
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    print(f"{i}: ", end="")
    print("{", end="")
    for j in range(len(graph[i])):
        if j != 0:
            print(", ", end="")
        print(f"{graph[i][j]}", end="")
    print("}")
