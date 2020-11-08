#!/usr/bin/env python3

def main():
    n = input()
    ans = 19
    for i in range(2 ** len(n)):
        tmp = 0
        cnt = 0
        for j in range(len(n)):
            if (i >> j) & 1 == 0:
                tmp += int(n[j])
                cnt += 1
        if tmp != 0 and tmp % 3 == 0:
            ans = min(ans, len(n) - cnt)
    print(ans if ans != 19 else -1)


if __name__ == "__main__":
    main()
