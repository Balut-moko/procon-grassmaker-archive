from sys import stdin
import numpy as np


def calc_degree_p2(p1, p2, p3):
    a = np.array(p1)
    b = np.array(p2)
    c = np.array(p3)
    vec_a = a - b
    vec_c = c - b

    length_vec_a = np.linalg.norm(vec_a)
    length_vec_c = np.linalg.norm(vec_c)
    inner_product = np.inner(vec_a, vec_c)
    cos = inner_product / (length_vec_a * length_vec_c)

    rad = np.arccos(cos)

    degree = np.rad2deg(rad)
    return degree


readline = stdin.readline
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
c = list(map(int, readline().split()))
d = list(map(int, readline().split()))
ans = "No"

b_deg = calc_degree_p2(a, b, c)
c_deg = calc_degree_p2(b, c, d)
d_deg = calc_degree_p2(c, d, a)
a_deg = calc_degree_p2(d, a, b)
if 359.01 < sum((a_deg, b_deg, c_deg, d_deg)) < 360.01:
    ans = "Yes"
print(ans)