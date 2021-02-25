def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if n < i * j:
                break
            for k in range(j, n + 1):
                if i * j * k <= n:
                    if i==j==k:
                        ans += 1
                    elif i==j or j==k:
                        ans += 3
                    else:
                        ans += 6
                else:
                    break

    print(ans)


if __name__ == "__main__":
    main()
