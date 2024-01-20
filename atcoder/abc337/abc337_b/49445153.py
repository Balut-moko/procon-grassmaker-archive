from itertools import product


S = input()

for a, b, c in product(range(101), repeat=3):
    T = "A" * a + "B" * b + "C" * c
    if S == T:
        print("Yes")
        exit()
print("No")
