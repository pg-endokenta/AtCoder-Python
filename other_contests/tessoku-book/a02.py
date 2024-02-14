n: int
x: int
a: list[int]

n, x = map(int, input().split())
a = list(map(int, input().split()))

for ai in a:
    if ai == x:
        print("Yes")
        exit()

print("No")