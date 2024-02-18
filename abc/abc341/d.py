import math

n: int
m: int
k: int
n, m, k = map(int, input().split())

left: int = min(n, m)
right: int = 10**50
lcm: int = math.lcm(n, m)

while left < right:
    mid: int = (left + right) // 2
    cnt: int = (mid // n) + (mid // m) - 2*(mid // lcm)

    if cnt < k:
        left = mid + 1
    elif cnt >= k:
        right = mid
print(left)
