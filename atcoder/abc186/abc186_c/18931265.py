def main():
    n = int(input())
    ans = n
    for i in range(n + 1):
        if "7" in str(i) or "7" in str(oct(i)):
            ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
