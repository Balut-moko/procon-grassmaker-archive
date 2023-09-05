from sys import stdin

readline = stdin.readline
s, t = readline().split()
lst = [
    "B9",
    "B8",
    "B7",
    "B6",
    "B5",
    "B4",
    "B3",
    "B2",
    "B1",
    "1F",
    "2F",
    "3F",
    "4F",
    "5F",
    "6F",
    "7F",
    "8F",
    "9F",
]
print(abs(lst.index(s) - lst.index(t)))