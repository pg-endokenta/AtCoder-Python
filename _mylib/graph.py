# グラフの頂点1と繋がっている最大頂点
from collections import defaultdict, deque

n: int
n = int(input())

graph = defaultdict(list)
a: int
b: int
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

seen: set[int] = set()
seen.add(1)
queue: deque[int] = deque()
queue.append(1)

while queue:
    v = queue.popleft()
    for next_v in graph[v]:
        if next_v not in seen:
            seen.add(next_v)
            queue.append(next_v)

print(max(seen))
