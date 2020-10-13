def main():
    a, b, c, d = map(int, input().split())
    if b / a > d / c:
        ans = 'TAKAHASHI'
    elif b / a < d / c:
        ans = 'AOKI'
    else:
        ans = 'DRAW'
    print(ans)


if __name__ == "__main__":
    main()
