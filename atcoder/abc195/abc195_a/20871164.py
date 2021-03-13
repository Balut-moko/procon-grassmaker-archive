#!/usr/bin/env python3

def main():
    m, h = map(int, input().split())
    if h % m == 0:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()
