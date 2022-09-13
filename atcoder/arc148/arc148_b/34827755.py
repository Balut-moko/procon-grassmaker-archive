from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]


def rotate_str(s):
    res = list(reversed(s))
    for i in range(len(res)):
        if res[i] == "d":
            res[i] = "p"
        else:
            res[i] = "d"
    return "".join(res)


def make_ans(l, r):
    res = s[:l]
    res += rotate_str(s[l:r])
    res += s[r:]
    return res


if s.count("p") == 0:
    print(s)
    exit()
first_idx = s.index("p")
ans = s
for i in range(first_idx, n + 1):
    ans = min(ans, make_ans(first_idx, i))
print(ans)
