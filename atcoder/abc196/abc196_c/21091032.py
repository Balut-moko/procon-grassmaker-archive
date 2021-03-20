#!/usr/bin/env python3

def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n**.5) + 100):
        if int(str(i) + str(i)) <= n:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
