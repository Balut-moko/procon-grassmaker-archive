def main():
    num = sorted(map(int, input().split()))

    cnt = 0
    a = num[2] - num[1]
    cnt += a
    num[0] += a

    if (num[2] - num[0]) % 2 == 0:
        cnt += (num[2] - num[0]) // 2
    else:
        cnt += (num[2] - num[0]) // 2 + 2

    print(cnt)


if __name__ == "__main__":
    main()