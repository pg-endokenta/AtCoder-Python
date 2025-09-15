x: int
c: int
x, c = map(int, input().split())

m = x // (1000 + c)

print(m * 1000)
