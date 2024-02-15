n: int
n = int(input())
a: list[int]
a = list(map(int, input().split()))

p: list[int] = [0] * (n+1)
p[1] = a[1-1]
for i in range(2, n+1):
    p[i] = max(p[i-1], a[i-1])

q: list[int] = [0] * (n+1)
q[n] = a[n-1]
for i in range(n-1, 0, -1):
    q[i] = max(q[i+1], a[i-1])


d: int
d = int(input())
l: int
r: int
for i in range(d):
    l, r = map(int, input().split())
    print(max(p[l-1], q[r+1]))
