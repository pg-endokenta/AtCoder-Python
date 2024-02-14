n: int
a: list[int]
n = int(input())
a = list(map(int, input().split()))

s: list[int] = [0]
for i in range(n):
    s.append(s[i]+a[i])


q: int
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    wins: int = s[r]-s[l-1]
    loses: int = (r-l+1) - wins
    
    if wins > loses:
        print("win")
    elif wins == loses:
        print("draw")
    else:
        print("lose")