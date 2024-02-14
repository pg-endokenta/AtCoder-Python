n: str
n = input()

ans: int = 0
for i in range(len(n), 0, -1):
    ans += int(n[i-1]) * (2**(len(n)-i))

print(ans)