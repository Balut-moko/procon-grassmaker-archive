from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
readline = stdin.readline
n = int(readline())
ans = 0


def dfs(i, flag3, flag5, flag7):
    global ans
    if i > n:
        return
    if all([flag3, flag5, flag7]):
        ans += 1
    dfs(i * 10 + 3, True, flag5, flag7)
    dfs(i * 10 + 5, flag3, True, flag7)
    dfs(i * 10 + 7, flag3, flag5, True)


dfs(0, False, False, False)
print(ans)
