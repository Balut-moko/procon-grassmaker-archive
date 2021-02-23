import collections


def main():
    n = int(input())
    v = list(map(int, input().split()))
    v_even = []
    v_odd = []
    for i in range(n):
        if i % 2 == 0:
            v_even.append(v[i])
        else:
            v_odd.append(v[i])
    cnt_v_even = collections.Counter(v_even)
    cnt_v_odd = collections.Counter(v_odd)
    if cnt_v_even.most_common()[0][0] == cnt_v_odd.most_common()[0][0]:
        if len(cnt_v_even) == 1 or len(cnt_v_odd) == 1:
            ans = n // 2
        else:
            ans = n - cnt_v_even.most_common(2)[0][1] - cnt_v_odd.most_common(2)[-1][1]
            ans = min(ans, n - cnt_v_even.most_common(2)[-1][1] - cnt_v_odd.most_common(2)[0][1])
    else:
        ans = n - cnt_v_even.most_common()[0][1] - cnt_v_odd.most_common()[0][1]

    print(ans)


if __name__ == "__main__":
    main()
