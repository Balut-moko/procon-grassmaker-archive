from sys import stdin

readline = stdin.readline
n = int(readline())
bit_li = ["0"] * 60 + list(bin(n)[2:])
bit_li = bit_li[-60:]
ans_set = {0}
n_bin_str = bin(n)

for i in range(60):
    if bit_li[i] == "1":
        tmp = pow(2, 59 - i)
        tmp_set = {0}
        for val in ans_set:
            tmp_set.add(val)
            tmp_set.add(val + tmp)
        ans_set = tmp_set

ans = sorted(ans_set)
for val in ans:
    print(val)
