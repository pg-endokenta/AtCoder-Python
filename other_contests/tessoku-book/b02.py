a: int
b: int

a, b = map(int, input().split())

for i in range(a, b + 1):
    if 100 % i == 0:
        print("Yes")
        exit()

print("No")