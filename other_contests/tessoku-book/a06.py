n: int
q: int
n, q = map(int, input().split())
a = list(map(int, input().split()))

s = []
s.append(0)
for i in range(n):
    s.append(s[i] + a[i])


left: int
right: int
for i in range(q):
    left, right = map(int, input().split())
    print(s[right] - s[left - 1])
