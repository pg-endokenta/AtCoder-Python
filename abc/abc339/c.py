n: int
a: list[int]

n = int(input())
a = list(map(int, input().split()))

min: int = 0
sum: int = 0

for i in range(n):
    sum += a[i]
    if sum < min:
        min = sum

if min < 0:
    print(abs(min) + sum)
else:
    print(sum)
