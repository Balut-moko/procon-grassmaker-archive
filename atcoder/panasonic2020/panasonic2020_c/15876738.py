def main():
    a, b, c = map(int, input().split())
    ans = 'No'
    if c - a - b >= 0 and 4 * a * b < (c - a - b) ** 2:
        ans = 'Yes'

    print(ans)


if __name__ == "__main__":
    main()
