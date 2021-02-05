import string


def main():
    n, m = map(int, input().split())
    name = input()
    kit = input()
    ans = 1
    for i in string.ascii_uppercase:
        if i in name and i not in kit:
            print(-1)
            return
        if i in name and i in kit:
            tmp = name.count(i) // kit.count(i)
            if name.count(i) % kit.count(i) != 0:
                tmp += 1
            ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
