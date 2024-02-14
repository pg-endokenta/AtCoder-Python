q: int
num1: int
num2: int
a: list[int] = []

q = int(input())

for i in range(q):
    num1, num2 = map(int, input().split())
    if num1 == 1:
        a.append(num2)
    if num1 == 2:
        print(a[-1 * num2])

