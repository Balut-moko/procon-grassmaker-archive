import collections


def main():
    S = input()
    cnt = 0
    tmp = ""
    for s in S:
        if s != tmp:
            cnt += 1
        tmp = s

    print(cnt - 1)


if __name__ == "__main__":
    main()