n: int
x: int
n, x = map(int, input().split())
a: list[int]
a = list(map(int, input().split()))


def search(x: int, a: list[int]) -> int:
    n: int
    n = len(a)
    left: int
    right: int
    left = 0
    right = n - 1
    while True:
        mid: int
        mid = (left + right) // 2
        if a[mid] > x:
            right = mid - 1
        elif a[mid] == x:
            return mid
        else:
            left = mid + 1


print(search(x, a) + 1)
