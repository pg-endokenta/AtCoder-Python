import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

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

visited: list[bool] = [False] * (n + 1)


def dfs(v: int) -> None:
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(e)


dfs(1)

for i in range(1, n + 1):
    if not visited[i]:
        print("The graph is not connected.")
        exit()

print("The graph is connected.")
