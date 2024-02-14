t: int
t = int(input())
n: int
n = int(input())

b: list[int] = [0] * (t+1)

l: int
r: int
for i in range(n):
    l, r = map(int, input().split())
    b[l] += 1
    b[r+1] -= 1

ans: int = 0
for i in range(t):
    ans += b[i]
    print(ans)
