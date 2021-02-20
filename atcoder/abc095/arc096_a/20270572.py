def main():
    a, b, c, x, y = map(int, input().split())
    if a + b <= 2 * c:
        ans = a * x + b * y
    else:
        if x <= y:
            ans = 2 * c * x + (y - x) * min(b, 2 * c)
        else:
            ans = 2 * c * y + (x - y) * min(a, 2 * c)

    print(ans)


if __name__ == "__main__":
    main()
