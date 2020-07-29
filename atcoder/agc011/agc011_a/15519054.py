#!/usr/bin/env python3

def main():
    N, C, K = map(int, input().split())
    T = sorted([int(input()) for i in range(N)])
    cnt = 0
    past_time = 0
    ans = 0
    for i in range(len(T)):
        if cnt != 0 and past_time != 0 and past_time + K < T[i]:
            ans += 1
            cnt = 1
            past_time = T[i]
        else:
            cnt += 1
            if cnt == 1:
                past_time = T[i]
            if cnt == C:
                ans += 1
                cnt = 0
    if cnt > 0:
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
