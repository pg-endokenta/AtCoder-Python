from collections import defaultdict

n: int = int(input())
a: list[int] = list(map(int, input().split()))
b: list[int] = list(map(int, input().split()))

dp: defaultdict[int, int] = defaultdict(int)

dp[1] = 0
dp[2] = a[0]
for i in range(3, n + 1):
    dp[i] = min(dp[i - 1] + a[i - 2], dp[i - 2] + b[i - 3])

print(dp[n])
