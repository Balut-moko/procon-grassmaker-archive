from sys import stdin


def calc_ans(n_str):
    n = int(n_str)
    ans = 10 ** (len(n_str) - 1) - 1

    for i in range(1, 10):
        t = n_str[:i]
        t1 = str(int(t) - 1)
        cnt = len(n_str) // i
        tt, tt1 = 0, 0
        if 2 <= cnt:
            tt = int(t * (len(n_str) // i))
            tt1 = int(t1 * (len(n_str) // i))
        if tt <= n:
            ans = max(ans, tt)
        if tt1 <= n:
            ans = max(ans, tt1)

    return ans


readline = stdin.readline
t = int(readline())

for _ in range(t):
    n_str = readline()[:-1]
    print(calc_ans(n_str))
