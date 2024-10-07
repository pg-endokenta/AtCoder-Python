t: int
t = int(input())
n: int
n = int(input())

b: list[int] = [0] * (t + 1)

left: int
right: int
for i in range(n):
    left, right = map(int, input().split())
    b[left] += 1
    b[right] -= 1

ans: int = 0
for i in range(t):
    ans += b[i]
    print(ans)
