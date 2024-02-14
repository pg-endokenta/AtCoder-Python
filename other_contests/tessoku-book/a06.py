n: int
q: int
n, q = map(int, input().split())
a = list(map(int, input().split()))

s = []
s.append(0)
for i in range(n):
    s.append(s[i]+a[i])


l: int
r: int
for i in range(q):
    l, r = map(int, input().split())
    print(s[r]-s[l-1])