def main():
    n, x = map(int, input().split())
    m = [int(input()) for i in range(n)]
    print(n + (x - sum(m)) // min(m))


if __name__ == "__main__":
    main()
