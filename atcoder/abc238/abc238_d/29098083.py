from sys import stdin


def check(a, s):
    a_bin_li = list(str(bin(a))[2:])[::-1]
    a_bin_li = a_bin_li + ["0"] * (60 - len(a_bin_li))
    s_bin_li = list(str(bin(s))[2:])[::-1]
    s_bin_li = s_bin_li + ["0"] * (60 - len(s_bin_li))

    inc = 0
    for i, v in enumerate(a_bin_li):
        if v == "1":
            if inc == 1:
                if s_bin_li[i] == "1":
                    continue
                else:
                    print("No")
                    return
            else:
                if s_bin_li[i] == "0":
                    inc = 1
                    continue
                else:
                    print("No")
                    return
        else:
            if inc == 1:
                if s_bin_li[i] == "1":
                    inc = 0
    if inc == 1:
        print("No")
        return
    print("Yes")


readline = stdin.readline
t = int(readline())
for _ in range(t):
    a, s = map(int, readline().split())
    check(a, s)
