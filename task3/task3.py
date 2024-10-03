m = int(input())
ans = 1
for i in range(1, int((2 * 10 ** 9) ** 0.5) + 1):
    if m % (i ** 2) == 0:
        ans = i ** 2
print(ans)
