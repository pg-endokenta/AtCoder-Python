import sys

sys.set_int_max_str_digits(200000)


n: int
n = int(input())
a: str
a = input()
b: str
b = input()

a_list: list[str] = list(a)
b_list: list[str] = list(b)

for i in range(n):
    if int(a_list[i]) > int(b_list[i]):
        tmp = a_list[i]
        a_list[i] = b_list[i]
        b_list[i] = tmp

a = "".join(a_list)
b = "".join(b_list)

ans: int = int(a) * int(b) % 998244353
print(ans)
