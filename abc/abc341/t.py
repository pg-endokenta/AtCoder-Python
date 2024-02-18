
n = 2
m = 3

start = 4
cnt_for_k = 0

if (n % start == 0 and m % start != 0):
    cnt_for_k += 1
elif (n % start != 0 and m % start == 0):
    cnt_for_k += 1

print(cnt_for_k)