S = list(input())
T = list(input())


def calc_length(S):
    if S[0] > S[1]:
        S = S[::-1]
    S[1] = chr(ord(S[1]) - ord(S[0]) + ord("A"))

    if S[1] == "B" or S[1] == "E":
        return 1
    if S[1] == "C" or S[1] == "D":
        return 2


if calc_length(S) == calc_length(T):
    print("Yes")
else:
    print("No")
