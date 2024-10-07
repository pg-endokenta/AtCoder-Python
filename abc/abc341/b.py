n: int = int(input())
a: list[int] = list(map(int, input().split()))


s: int
t: int
for i in range(n - 1):
    s, t = map(int, input().split())
    a[i + 1] = a[i + 1] + (a[i] // s) * t

print(a[n - 1])
