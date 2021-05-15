#!/usr/bin/env python3

def main():
    a = sorted(map(int, input().split()))
    ans = 'No'
    if a[2] - a[1] == a[1] - a[0]:
        ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    main()
