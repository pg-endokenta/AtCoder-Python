n: int
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if i != j and j != k and k != i:
                if a[i] + a[j] + a[k] == 1000:
                    print("Yes")
                    exit()

print("No")
