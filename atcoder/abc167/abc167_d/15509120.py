#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    Acnt = [0] * N
    Acnt[0] = 1
    telepo = [1]
    i = 0
    while True:
        Acnt[A[i] - 1] += 1
        if Acnt[A[i] - 1] > 1:
            break
        telepo.append(A[i])
        i = A[i] - 1
    roop_s = telepo.index(A[i])
    roop = len(telepo) - roop_s

    ans = 0
    if K < roop_s:
        ans = K
    else:
        ans = K - roop_s
        ans %= roop
        ans += roop_s

    print(telepo[ans])


if __name__ == "__main__":
    main()
