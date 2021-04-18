#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())
    ans = [0] * (a + b)

    for i in range(a):
        ans[i] = i + 1
    for j in range(b):
        ans[a + b - j - 1] = -j - 1
    tmp = sum(ans)
    if tmp >= 0:
        ans[-1] -= tmp
    else:
        ans[0] -= tmp
    print(*ans)


if __name__ == "__main__":
    main()
