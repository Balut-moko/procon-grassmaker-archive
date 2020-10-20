def main():
    a, b = map(int, input().split())
    print('IMPOSSIBLE' if (a - b) % 2 else abs(a + b) // 2)


if __name__ == "__main__":
    main()
