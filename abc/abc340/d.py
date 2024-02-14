import heapq

n: int
n = int(input())

graph: list[list[tuple[int, int]]] = [[] for _ in range(n+1)]

a: int
b: int
x: int
for i in range(1, n):
    a, b, x = map(int, input().split())
    graph[i].append((i+1, a))
    graph[i].append((x, b))


INF = 10**18
done = [False] * (n+1)
cur = [INF] * (n+1)
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

print(cur[n])
