#!/usr/bin/env python3

def main():
    n = int(input())
    st = []
    for _ in range(n):
        s, t = input().split()
        st.append([s, int(t)])
    st = sorted(st, key=lambda x: x[1])

    print(st[-2][0])


if __name__ == "__main__":
    main()
