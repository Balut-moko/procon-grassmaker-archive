#!/usr/bin/env python3
def Base_n_to_10(X, n):
    out = 0
    for i in range(1, len(str(X)) + 1):
        out += int(X[-i]) * (n**(i - 1))
    return out


def solve(mid, X, M):
    if Base_n_to_10(X, mid) <= M:
        return True
    else:
        return False


def meguru_bisect(ok, ng, X, M):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if solve(mid, X, M):
            ok = mid
        else:
            ng = mid
    return ok


def main():
    X = input()
    M = int(input())
    x_list = sorted(X)
    d = int(x_list[-1])
    if len(X) == 1:
        if int(X) <= M:
            ans = 1
        else:
            ans = 0
    else:
        ans = meguru_bisect(d, M + 1, X, M) - d

    print(ans)


if __name__ == "__main__":
    main()
