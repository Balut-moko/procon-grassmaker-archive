from sys import stdin


def calc_next(S):
    N = len(S)
    res = [[N] * 26 for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(26):
            res[i][j] = res[i + 1][j]
        res[i][ord(S[i]) - ord("a")] = i
    return res


readline = stdin.readline
n = int(readline())
s = list(readline()[:-1])
s_reverse = s[::-1]
nex = calc_next(s_reverse)
ans = s.copy()
left, right = 0, 0

while True:
    for i in range(26):
        if nex[right][i] != n and nex[right][i] + left < n:
            s_min = chr(ord("a") + i)
            nxt_r = n - nex[right][i] - 1
            nxt_l = left
            for j in range(left, nxt_r):
                if s_min < s[j]:
                    nxt_l = j
                    break

            if nxt_l < nxt_r and ans[nxt_l] > ans[nxt_r]:
                ans[nxt_l], ans[nxt_r] = ans[nxt_r], ans[nxt_l]
                left = nxt_l + 1
                right = n - nxt_r
                break
            else:
                left += 1
                continue
    else:
        break

print(*ans, sep="")
