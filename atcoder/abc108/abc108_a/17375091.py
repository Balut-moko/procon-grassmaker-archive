def main():
    k = int(input())
    a = k // 2
    print(a**2 if k % 2 == 0 else a * (a + 1))


if __name__ == "__main__":
    main()
