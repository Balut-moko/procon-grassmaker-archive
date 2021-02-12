def main():
    S = input().split()
    n = int(input())
    T = [input() for _ in range(n)]

    for s in S:
        for t in T:
            if len(s) == len(t):
                for i in range(len(s)):
                    if t[i] == '*':
                        continue
                    if t[i] != s[i]:
                        break
                else:
                    print('*' * len(s))
                    break
        else:
            print(s)


if __name__ == "__main__":
    main()
