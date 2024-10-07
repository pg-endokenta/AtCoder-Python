from collections import deque

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

dist: list[int] = [-1] * (n + 1)

q: deque[int] = deque()
q.append(1)
dist[1] = 0

while len(q) > 0:
    v = q.popleft()
    for e in graph[v]:
        if dist[e] == -1:
            dist[e] = dist[v] + 1
            q.append(e)

for i in range(1, n + 1):
    print(dist[i])
