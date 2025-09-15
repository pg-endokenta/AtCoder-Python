n: int = int(input())
l: list[int] = list(map(int, input().split()))


def first_last_one(a: list[int]) -> tuple[int | None, int | None]:
    """最初と最後の1のindexを返す."""
    first = last = None
    for i, v in enumerate(a):
        if v == 1:
            if first is None:
                first = i
            last = i
    return first, last


first, last = first_last_one(l)
if first is None or last is None:
    print(0)
else:
    print(last - first)
