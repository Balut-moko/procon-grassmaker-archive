def main():
    n, D, H = map(int, input().split())
    ans = 0
    for i in range(n):
        d, h = map(int, input().split())
        h -= d * (H - h) / (D - d)
        if ans < h:
            ans = h
    print(ans)


if __name__ == "__main__":
    main()
