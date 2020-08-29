#!/usr/bin/env python3

def main():
    D, T, S = map(int, input().split())
    if D/S <= T:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)


if __name__ == "__main__":
    main()
