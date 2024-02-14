import heapq

n: int
m: int
n, m = map(int, input().split())

graph: list[list[tuple[int, int]]] = [[] for _ in range(n+1)]

a: int
b: int
c: int
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF: int = 10**18
done: list[bool] = [False] * (n+1)
cur: list[int] = [INF] * (n+1)
cur[1] = 0
q: list[tuple[int, int]] = []
heapq.heappush(q, (cur[1], 1))

while len(q) > 0:
    d, v = heapq.heappop(q)
    if done[v]:
        continue
    done[v] = True
    for next_v, c in graph[v]:
        if cur[next_v] > cur[v] + c:
            cur[next_v] = cur[v] + c
            heapq.heappush(q, (cur[next_v], next_v))

for i in range(1, n+1):
    if cur[i] == INF:
        print("-1")
    else:
        print(cur[i])