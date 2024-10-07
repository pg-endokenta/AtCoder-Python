from collections import defaultdict

n: int
k: int
n, k = map(int, input().split())
a: list[int] = [0] + list(map(int, input().split()))

r: defaultdict[int, int] = defaultdict(int)

for i in range(1, n):
    if i == 1:
        r[i] = 1
    else:
        r[i] = r[i - 1]

    while (r[i] < n) and (a[r[i] + 1] - a[i] <= k):
        r[i] += 1

ans: int = 0

for i in range(1, n):
    ans += r[i] - i

print(ans)
