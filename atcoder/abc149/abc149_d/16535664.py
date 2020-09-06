#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    c = ""
    ans = 0

    for i in range(n):
        if t[i] == "r":
            if i >= k and c[i-k] == 'p':
                c += 'x'
            else:
                c += "p"
                ans += p
        elif t[i] == "s":
            if i >= k and c[i-k] == 'r':
                c += 'x'
            else:
                c += "r"
                ans += r
        else:
            if i >= k and c[i-k] == 's':
                c += 'x'
            else:
                c += "s"
                ans += s
    print(ans)


if __name__ == "__main__":
    main()
