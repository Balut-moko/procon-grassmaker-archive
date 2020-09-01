def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0] * n
    for i in range(n):
        c[i] = a[i] - b[i]
    c.sort()
    i = 0
    j = n - 1
    cnt = 0
    tmp = c[i] + c[j]
    while i != j:
        if c[i] < 0:
            if tmp >= 0:
                cnt += 1
                i += 1
                tmp += c[i]
            else:
                cnt += 1
                j -= 1
                tmp += c[j]
        else:
            break
    if tmp >= 0:
        print(cnt + 1 if cnt > 0 else 0)
    else:
        print(-1)


if __name__ == "__main__":
    main()
