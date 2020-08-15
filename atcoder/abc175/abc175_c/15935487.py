#!/usr/bin/env python3

def main():
    X, K, D = map(int, input().split())

    cnt = abs(X) // D
    if X >= 0:
        X -= min(K, cnt) * D
    else:
        X += min(K, cnt) * D

    K -= min(K, cnt)
    if K % 2 == 0:
        ans = abs(X)
    else:
        ans = min(abs(X - D), abs(X + D))
    print(ans)


if __name__ == "__main__":
    main()
