#!/usr/bin/env python3

def main():
    N = int(input())
    c = input()
    ans = 0
    j = N - 1
    for i in range(N):
        if c[i] == 'W':
            while j > i:
                if c[j] == 'R':
                    ans += 1
                    j -= 1
                    break
                j -= 1
            else:
                break
    print(ans)


if __name__ == "__main__":
    main()
