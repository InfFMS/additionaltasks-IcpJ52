from math import ceil
n = int(input())
s = n * (n + 1) // 2
if s % 2 == 1:
    print('IMPOSSIBLE')
else:
    s //= 2
    k = ceil((1 + (1 + 8 * s) ** 0.5) / 2)
    b = s - (n + k) * (n - k + 1) // 2
    if b == 0:
        print('+' * (k - 1) + '-' * (n - k + 1))
    else:
        print('+' * (b - 1) + '-' + '+' * (k - b - 1) + '-' * (n - k + 1))
