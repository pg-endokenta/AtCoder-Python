n: int
k: int
n, k = map(int, input().split())
a: list[int] = list(map(int, input().split()))


def check(p: int) -> bool:
    cnt: int = 0
    for i in range(n):
        cnt += p // a[i]
    if cnt >= k:
        return True
    return False


left: int = 0
right: int = 1000000000
while left < right:
    mid: int = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1

print(left)
