d: int
d = int(input())
n: int
n = int(input())

b: list[int] = [0] * (d+2)

l: int
r: int
for i in range(n):
    l, r = map(int, input().split())
    b[l] += 1
    b[r+1] -= 1

ans: int = 0
for i in range(1, d+1):
    ans += b[i]
    print(ans)