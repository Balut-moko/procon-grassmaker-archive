def main():
    a, b = map(int, input().split())
    print(b - a if b % a else a + b)


if __name__ == "__main__":
    main()
