n: int
n = int(input())

for i in range(9, -1, -1):
    print(n // (2**i) % 2, end="")

print()
