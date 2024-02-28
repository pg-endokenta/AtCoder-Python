from collections import defaultdict

n: int
k: int
n, k = map(int, input().split())
a: list[int] =[0] + list(map(int, input().split()))

b: defaultdict[int, int] = defaultdict(int)

b[0] = 0
for i in range(1, n+1):
    b[i] = a[i] + b[i-1]


r: defaultdict[int, int] = defaultdict(int)

for i in range(1, n+1):
    if i == 1:
        r[i] = 0
    else:
        r[i] = r[i-1]
    
    while (r[i] < n) and (b[r[i]+1] - b[i-1] <= k):
        r[i] += 1


ans: int = 0
for i in range(1, n+1):
    ans += (r[i] - i + 1)

print(ans)
