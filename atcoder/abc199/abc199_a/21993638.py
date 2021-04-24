#!/usr/bin/env python3

def main():
    a, b, c = map(int, input().split())
    if a * a + b * b < c * c:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()
