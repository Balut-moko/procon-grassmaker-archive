#!/usr/bin/env python3


def main():
    x = int(input())
    ans, mod = divmod(x, 11)
    ans *= 2
    if mod >= 7:
        ans += 2
    elif mod > 0:
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
