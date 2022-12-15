from sys import stdin


def makeStr(nums):
    res = ""
    for i in range(len(nums)):
        res += chr((ord("a") + nums[i]))
    return make_std(res)


def make_std(s):
    s_li = list(s)
    di = dict()
    cnt = 0
    for val in s:
        if val not in di.keys():
            di[val] = chr(ord("a") + cnt)
            cnt += 1
    for i, val in enumerate(s_li):
        s_li[i] = di[val]
    return "".join(s_li)


readline = stdin.readline
n = int(readline())
ans = set()
ans.add("a")

for i in range(n - 1):
    tmp = ans.copy()
    tmp2 = set()
    for val in tmp:
        tmp2.add(make_std("a" + val))
    for j in range(i + 2):
        for val in tmp:
            val = val + chr(ord("a") + j)
            tmp2.add(make_std(val))
    ans = tmp2
ans = sorted(ans)
print(*ans, sep="\n")
