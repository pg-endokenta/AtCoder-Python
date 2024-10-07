n: int
a: list[int]
n = int(input())
a = list(map(int, input().split()))

s: list[int] = [0]
for i in range(n):
    s.append(s[i] + a[i])


q: int
q = int(input())
for i in range(q):
    left, right = map(int, input().split())
    wins: int = s[right] - s[left - 1]
    loses: int = (right - left + 1) - wins

    if wins > loses:
        print("win")
    elif wins == loses:
        print("draw")
    else:
        print("lose")
