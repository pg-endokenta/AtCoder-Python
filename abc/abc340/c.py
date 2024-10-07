n: int

n = int(input())
d: dict[int, int] = {1: 0, 2: 2}


def f(n: int) -> int:
    if n in d:
        return d[n]

    ans = n + f(n // 2) + f((n + 1) // 2)
    d[n] = ans
    return ans


print(f(n))
