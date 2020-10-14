import math


def main():
    menu = [int(input()) for _ in range(5)]
    loss = [a % 10 for a in menu if a % 10 != 0]
    if loss:
        ans = sum([math.ceil(a / 10) * 10 for a in menu]) + min(loss) - 10
    else:
        ans = sum([math.ceil(a / 10) * 10 for a in menu])
    print(ans)


if __name__ == "__main__":
    main()
