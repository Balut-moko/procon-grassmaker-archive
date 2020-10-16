def main():
    n = int(input())
    S = input()
    ans = ""
    for s in S:
        ans += chr(65 + (ord(s) - 65 + n) % 26)
    print(ans)


if __name__ == "__main__":
    main()
