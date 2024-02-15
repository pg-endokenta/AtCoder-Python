n: int = int(input())


def check(x: float) -> bool:
    if x**3 + x >= n:
        return True
    return False


left: float = 0
right: float = 100

mid: float = 50
while abs(mid**3 + mid - n) > 0.001:
    mid = (left + right) / 2
    if check(mid):
        right = mid
    else:
        left = mid

print(mid)
