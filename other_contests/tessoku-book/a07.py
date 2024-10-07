d: int
d = int(input())
n: int
n = int(input())

b: list[int] = [0] * (d + 2)

left: int
right: int
for i in range(n):
    left, right = map(int, input().split())
    b[left] += 1
    b[right + 1] -= 1

ans: int = 0
for i in range(1, d + 1):
    ans += b[i]
    print(ans)
