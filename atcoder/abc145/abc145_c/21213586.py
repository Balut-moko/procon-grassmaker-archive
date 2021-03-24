import itertools


def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    tmp = 0
    p_list = list(itertools.permutations(range(n)))
    for val in p_list:
        for i in range(1, len(val)):
            tmp += ((xy[val[i - 1]][0] - xy[val[i]][0])**2 + (xy[val[i - 1]][1] - xy[val[i]][1])**2)**.5
    print(tmp / len(p_list))


if __name__ == "__main__":
    main()
