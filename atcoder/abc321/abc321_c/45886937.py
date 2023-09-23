def has_bit(n, i):
    return n & (1 << i) > 0


nums = []
for n in range(2, 1 << 10):
    x = 0
    for i in range(9, -1, -1):
        if has_bit(n, i):
            x *= 10
            x += i
    nums.append(x)

nums.sort()
k = int(input())
print(nums[k - 1])
