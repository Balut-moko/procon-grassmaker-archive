def func(n):
    n_str = str(n)
    ans = 0
    for i in range(len(n_str)):
        ans += int(n_str[i]) * n ** (len(n_str) - 1 - i)
    return ans


def main():
    A = int(input())
    for k in range(10, 10001):
        if A == func(k):
            ans = k
            break
    else:
        ans = -1
    print(ans)


if __name__ == "__main__":
    main()
