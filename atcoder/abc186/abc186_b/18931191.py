def main():
    h, w = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(h)]
    min_num = min([min(a) for a in A])
    ans = sum([sum(a) - min_num * w for a in A])
    print(ans)


if __name__ == "__main__":
    main()
