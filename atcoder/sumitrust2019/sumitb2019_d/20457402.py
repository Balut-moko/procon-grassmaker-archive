import collections


def main():
    n = int(input())
    s = input()
    ans = set()
    for i in range(10):
        i_index = s.find(str(i))
        if i_index == -1:
            continue
        for j in range(10):
            j_index = s.find(str(j), i_index + 1)
            if j_index == -1:
                continue
            for k in range(10):
                k_index = s.find(str(k), j_index + 1)
                if k_index == -1:
                    continue
                ans.add((i, j, k))

    print(len(ans))


if __name__ == "__main__":
    main()
