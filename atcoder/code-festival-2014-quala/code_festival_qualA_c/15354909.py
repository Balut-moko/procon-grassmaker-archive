def main():
    A, B = map(int, input().split())
    A -= 1
    ans = 0
    ans += B // 4 - B // 100 + B // 400
    ans -= A // 4 - A // 100 + A // 400
    print(ans)


if __name__ == "__main__":
    main()