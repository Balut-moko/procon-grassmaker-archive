def main():
    a, b, c = map(int, input().split())
    ans = "NO"
    for i in range(1, b + 1):
        if a * i % b == c:
            ans = "YES"
    print(ans)


if __name__ == "__main__":
    main()
